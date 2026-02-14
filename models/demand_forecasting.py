"""
Demand Forecasting Models
Contains ML models for inventory demand prediction and reorder optimization
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta


def forecast_demand(demand_data, product_id, days_ahead=14):
    """
    Forecast demand using time series analysis
    
    Args:
        demand_data: Historical demand dataframe
        product_id: Product ID to forecast
        days_ahead: Number of days to forecast
        
    Returns:
        dict with historical data, forecast, and confidence intervals
    """
    # Filter data for specific product
    product_demand = demand_data[demand_data['product_id'] == product_id].copy()
    
    # If no data, generate sample
    if len(product_demand) == 0:
        dates = pd.date_range(end=datetime.now(), periods=60, freq='D')
        demand_values = np.random.poisson(lam=150, size=60) + np.random.randint(-20, 20, 60)
        product_demand = pd.DataFrame({
            'date': dates,
            'demand': demand_values
        })
    
    # Sort by date
    product_demand = product_demand.sort_values('date')
    
    # Calculate trend
    recent_demand = product_demand['demand'].tail(30).values
    trend = np.polyfit(range(len(recent_demand)), recent_demand, 1)[0]
    
    # Calculate seasonality (weekly pattern)
    product_demand['day_of_week'] = pd.to_datetime(product_demand['date']).dt.dayofweek
    weekly_pattern = product_demand.groupby('day_of_week')['demand'].mean()
    
    # Base forecast
    last_demand = recent_demand.mean()
    
    # Generate forecast
    forecast_dates = pd.date_range(
        start=product_demand['date'].max() + timedelta(days=1),
        periods=days_ahead,
        freq='D'
    )
    
    forecast_values = []
    for i, date in enumerate(forecast_dates):
        day_of_week = date.dayofweek
        
        # Base prediction with trend
        base_forecast = last_demand + (trend * i)
        
        # Add weekly seasonality
        seasonal_factor = weekly_pattern[day_of_week] / last_demand if day_of_week in weekly_pattern.index else 1.0
        
        # Add some random variation
        noise = np.random.normal(0, 5)
        
        forecast = base_forecast * seasonal_factor + noise
        forecast = max(0, forecast)  # Cannot be negative
        
        forecast_values.append(forecast)
    
    # Calculate confidence intervals (simulated)
    std_dev = recent_demand.std()
    confidence_upper = [f + 1.96 * std_dev for f in forecast_values]
    confidence_lower = [max(0, f - 1.96 * std_dev) for f in forecast_values]
    
    return {
        'historical_dates': product_demand['date'].tolist(),
        'historical_demand': product_demand['demand'].tolist(),
        'forecast_dates': forecast_dates.tolist(),
        'forecast_demand': forecast_values,
        'confidence_upper': confidence_upper,
        'confidence_lower': confidence_lower,
        'trend': trend,
        'avg_demand': last_demand
    }


def calculate_reorder_point(product_row):
    """
    Calculate optimal reorder point and quantity
    
    Args:
        product_row: Product data from inventory dataframe
        
    Returns:
        dict with reorder recommendations
    """
    # Economic Order Quantity (EOQ) calculation
    annual_demand = 365 * 10  # Assuming ~10 units/day average
    ordering_cost = 100  # Fixed cost per order (JOD)
    holding_cost = product_row['unit_cost'] * 0.25  # 25% of unit cost annually
    
    # EOQ formula: sqrt((2 * D * S) / H)
    eoq = np.sqrt((2 * annual_demand * ordering_cost) / holding_cost)
    
    # Reorder point = (Average daily demand * Lead time) + Safety stock
    avg_daily_demand = 10  # Simulated
    lead_time = product_row['lead_time_days']
    safety_stock = product_row['safety_stock']
    
    reorder_point = (avg_daily_demand * lead_time) + safety_stock
    
    # Predicted weekly demand (simulated with some variation)
    predicted_demand = avg_daily_demand * 7 * np.random.uniform(0.8, 1.2)
    
    # Recommended reorder quantity
    # If stock is very low, order more
    current_stock = product_row['current_stock']
    stock_deficit = max(0, safety_stock - current_stock)
    
    reorder_quantity = eoq + stock_deficit
    
    return {
        'reorder_point': reorder_point,
        'reorder_quantity': reorder_quantity,
        'economic_order_qty': eoq,
        'predicted_demand': predicted_demand,
        'safety_stock': safety_stock,
        'lead_time': lead_time,
        'current_stock': current_stock
    }


def calculate_inventory_health(inventory_data):
    """
    Calculate overall inventory health score
    
    Args:
        inventory_data: Inventory dataframe
        
    Returns:
        float: Health score (0-100)
    """
    # Factors for health calculation
    
    # 1. Stock level adequacy (40%)
    above_safety = (inventory_data['current_stock'] >= inventory_data['safety_stock']).sum()
    stock_adequacy = (above_safety / len(inventory_data)) * 40
    
    # 2. Turnover efficiency (30%)
    # Ideal: not too much overstock
    overstock = (inventory_data['current_stock'] > inventory_data['safety_stock'] * 3).sum()
    turnover_score = ((len(inventory_data) - overstock) / len(inventory_data)) * 30
    
    # 3. Value distribution (30%)
    # Not too much capital tied up in single items
    inventory_data['stock_value'] = inventory_data['current_stock'] * inventory_data['unit_cost']
    max_value_ratio = inventory_data['stock_value'].max() / inventory_data['stock_value'].sum()
    distribution_score = (1 - max_value_ratio) * 30 if max_value_ratio < 0.5 else 15
    
    health_score = stock_adequacy + turnover_score + distribution_score
    
    return health_score


def identify_slow_moving_items(inventory_data, demand_data, threshold_days=90):
    """
    Identify slow-moving inventory items
    
    Args:
        inventory_data: Inventory dataframe
        demand_data: Demand dataframe
        threshold_days: Days without demand to be considered slow-moving
        
    Returns:
        list of product IDs
    """
    slow_moving = []
    
    recent_date = demand_data['date'].max()
    cutoff_date = recent_date - timedelta(days=threshold_days)
    
    for product_id in inventory_data['product_id']:
        recent_demand = demand_data[
            (demand_data['product_id'] == product_id) &
            (demand_data['date'] >= cutoff_date)
        ]
        
        if len(recent_demand) == 0 or recent_demand['demand'].sum() < 10:
            slow_moving.append(product_id)
    
    return slow_moving


def optimize_safety_stock(product_row, demand_volatility='medium'):
    """
    Calculate optimal safety stock level
    
    Args:
        product_row: Product data
        demand_volatility: 'low', 'medium', or 'high'
        
    Returns:
        int: Recommended safety stock level
    """
    # Service level (Z-score)
    service_levels = {
        'low': 1.28,      # 90% service level
        'medium': 1.65,   # 95% service level
        'high': 2.33      # 99% service level
    }
    
    z_score = service_levels.get(demand_volatility, 1.65)
    
    # Assumed demand statistics
    avg_daily_demand = 10
    demand_std = avg_daily_demand * 0.3  # 30% coefficient of variation
    lead_time = product_row['lead_time_days']
    
    # Safety stock formula: Z * σ * sqrt(LT)
    safety_stock = z_score * demand_std * np.sqrt(lead_time)
    
    return int(safety_stock)
