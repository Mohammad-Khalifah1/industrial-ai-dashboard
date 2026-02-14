"""
Calculation Utilities
Business logic calculations for metrics and KPIs
"""

import numpy as np
import pandas as pd


def calculate_health_score(machine_data):
    """
    Calculate overall machine health score
    
    Args:
        machine_data: Machine dataframe
        
    Returns:
        float: Health score (0-100)
    """
    # Temperature score (40% weight)
    # Ideal: 60-75°C, Max safe: 85°C
    temp_scores = machine_data['temperature'].apply(
        lambda x: 100 if x <= 75 else max(0, 100 - (x - 75) * 5)
    )
    temp_score = temp_scores.mean() * 0.40
    
    # Vibration score (35% weight)
    # Ideal: 0.5-2.5 mm/s, Max safe: 3.5 mm/s
    vib_scores = machine_data['vibration'].apply(
        lambda x: 100 if x <= 2.5 else max(0, 100 - (x - 2.5) * 20)
    )
    vib_score = vib_scores.mean() * 0.35
    
    # Operational hours score (25% weight)
    # Fresh: 0-3000h, Aged: 7000h+
    hours_scores = machine_data['operational_hours'].apply(
        lambda x: 100 if x <= 3000 else max(0, 100 - (x - 3000) / 50)
    )
    hours_score = hours_scores.mean() * 0.25
    
    total_score = temp_score + vib_score + hours_score
    
    return total_score


def calculate_mtbf(machine_data, failure_threshold=0.6):
    """
    Calculate Mean Time Between Failures
    
    Args:
        machine_data: Machine dataframe
        failure_threshold: Probability threshold for failure
        
    Returns:
        float: MTBF in hours
    """
    # Simplified MTBF calculation
    total_operating_hours = machine_data['operational_hours'].sum()
    
    # Estimate failures based on condition
    critical_machines = len(machine_data[machine_data['temperature'] > 85])
    estimated_failures = critical_machines * 1.5  # Assume 1.5 failures per critical machine
    
    if estimated_failures == 0:
        return float('inf')
    
    mtbf = total_operating_hours / estimated_failures
    
    return mtbf


def calculate_oee(availability=0.95, performance=0.90, quality=0.98):
    """
    Calculate Overall Equipment Effectiveness
    
    Args:
        availability: % of time equipment is available
        performance: % of target performance achieved
        quality: % of good quality output
        
    Returns:
        float: OEE percentage
    """
    oee = availability * performance * quality * 100
    return oee


def calculate_inventory_turnover(inventory_data, annual_demand=None):
    """
    Calculate inventory turnover ratio
    
    Args:
        inventory_data: Inventory dataframe
        annual_demand: Annual demand (if None, estimated)
        
    Returns:
        float: Turnover ratio
    """
    # Cost of goods sold (COGS) - estimated
    if annual_demand is None:
        # Assume each product sells 10 units/day on average
        annual_demand = 365 * 10 * len(inventory_data)
    
    avg_unit_cost = inventory_data['unit_cost'].mean()
    cogs = annual_demand * avg_unit_cost
    
    # Average inventory value
    avg_inventory_value = (inventory_data['current_stock'] * inventory_data['unit_cost']).sum()
    
    # Turnover ratio
    if avg_inventory_value == 0:
        return 0
    
    turnover_ratio = cogs / avg_inventory_value
    
    return turnover_ratio


def calculate_days_of_inventory(inventory_turnover):
    """
    Calculate days of inventory on hand
    
    Args:
        inventory_turnover: Turnover ratio
        
    Returns:
        float: Days of inventory
    """
    if inventory_turnover == 0:
        return float('inf')
    
    days = 365 / inventory_turnover
    return days


def calculate_fill_rate(demand_met, total_demand):
    """
    Calculate order fill rate
    
    Args:
        demand_met: Units of demand fulfilled
        total_demand: Total units demanded
        
    Returns:
        float: Fill rate percentage
    """
    if total_demand == 0:
        return 100.0
    
    fill_rate = (demand_met / total_demand) * 100
    return fill_rate


def calculate_carrying_cost(inventory_data, annual_rate=0.25):
    """
    Calculate annual carrying cost
    
    Args:
        inventory_data: Inventory dataframe
        annual_rate: Annual carrying cost as % of inventory value
        
    Returns:
        float: Annual carrying cost
    """
    total_inventory_value = (inventory_data['current_stock'] * 
                            inventory_data['unit_cost']).sum()
    
    carrying_cost = total_inventory_value * annual_rate
    
    return carrying_cost


def calculate_stockout_cost(stockout_days, daily_demand, unit_price, lost_sale_rate=0.30):
    """
    Calculate cost of stockout
    
    Args:
        stockout_days: Number of days out of stock
        daily_demand: Average daily demand
        unit_price: Price per unit
        lost_sale_rate: % of demand lost during stockout
        
    Returns:
        float: Stockout cost
    """
    lost_sales = stockout_days * daily_demand * lost_sale_rate
    stockout_cost = lost_sales * unit_price
    
    return stockout_cost


def calculate_safety_stock_cost(safety_stock_units, unit_cost, holding_cost_rate=0.25):
    """
    Calculate annual cost of holding safety stock
    
    Args:
        safety_stock_units: Units in safety stock
        unit_cost: Cost per unit
        holding_cost_rate: Annual holding cost rate
        
    Returns:
        float: Annual safety stock cost
    """
    safety_stock_value = safety_stock_units * unit_cost
    annual_cost = safety_stock_value * holding_cost_rate
    
    return annual_cost


def calculate_reorder_cost(num_orders, cost_per_order=100):
    """
    Calculate annual reorder cost
    
    Args:
        num_orders: Number of orders per year
        cost_per_order: Fixed cost per order
        
    Returns:
        float: Annual reorder cost
    """
    return num_orders * cost_per_order


def calculate_total_cost(holding_cost, ordering_cost, stockout_cost=0):
    """
    Calculate total inventory cost
    
    Args:
        holding_cost: Annual holding cost
        ordering_cost: Annual ordering cost
        stockout_cost: Annual stockout cost
        
    Returns:
        float: Total cost
    """
    return holding_cost + ordering_cost + stockout_cost


def calculate_service_level(orders_fulfilled, total_orders):
    """
    Calculate service level
    
    Args:
        orders_fulfilled: Number of orders fulfilled on time
        total_orders: Total number of orders
        
    Returns:
        float: Service level percentage
    """
    if total_orders == 0:
        return 100.0
    
    service_level = (orders_fulfilled / total_orders) * 100
    return service_level


def calculate_warehouse_utilization(used_space, total_space):
    """
    Calculate warehouse space utilization
    
    Args:
        used_space: Space currently in use
        total_space: Total available space
        
    Returns:
        float: Utilization percentage
    """
    if total_space == 0:
        return 0
    
    utilization = (used_space / total_space) * 100
    return utilization


def calculate_labor_productivity(units_processed, labor_hours):
    """
    Calculate labor productivity
    
    Args:
        units_processed: Number of units processed
        labor_hours: Total labor hours
        
    Returns:
        float: Units per labor hour
    """
    if labor_hours == 0:
        return 0
    
    productivity = units_processed / labor_hours
    return productivity


def calculate_cost_per_unit(total_cost, units_produced):
    """
    Calculate cost per unit
    
    Args:
        total_cost: Total operational cost
        units_produced: Number of units produced
        
    Returns:
        float: Cost per unit
    """
    if units_produced == 0:
        return 0
    
    cost_per_unit = total_cost / units_produced
    return cost_per_unit


def calculate_downtime_cost(downtime_hours, production_rate, unit_value):
    """
    Calculate cost of downtime
    
    Args:
        downtime_hours: Hours of downtime
        production_rate: Units per hour
        unit_value: Value per unit
        
    Returns:
        float: Downtime cost
    """
    lost_production = downtime_hours * production_rate
    downtime_cost = lost_production * unit_value
    
    return downtime_cost


def calculate_maintenance_efficiency(planned_maintenance_hours, 
                                    total_maintenance_hours):
    """
    Calculate maintenance efficiency
    
    Args:
        planned_maintenance_hours: Hours of planned maintenance
        total_maintenance_hours: Total maintenance hours (planned + unplanned)
        
    Returns:
        float: Efficiency percentage
    """
    if total_maintenance_hours == 0:
        return 100.0
    
    efficiency = (planned_maintenance_hours / total_maintenance_hours) * 100
    return efficiency
