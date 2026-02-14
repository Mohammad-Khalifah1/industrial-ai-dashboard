"""
Data Processing Utilities
Functions for loading, generating, and processing data
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta


def load_data():
    """
    Load data from CSV files
    
    Returns:
        tuple: (inventory_df, machines_df, demand_df, operations_df)
    """
    try:
        inventory_df = pd.read_csv('data/inventory_data.csv')
        machines_df = pd.read_csv('data/machinery_data.csv')
        demand_df = pd.read_csv('data/demand_history.csv')
        operations_df = pd.read_csv('data/operations_data.csv')
        
        # Convert date columns
        if 'date' in demand_df.columns:
            demand_df['date'] = pd.to_datetime(demand_df['date'])
        
        return inventory_df, machines_df, demand_df, operations_df
    
    except FileNotFoundError:
        # If files don't exist, generate demo data
        return generate_demo_data()


def generate_demo_data():
    """
    Generate realistic demo data for the warehouse
    
    Returns:
        tuple: (inventory_df, machines_df, demand_df, operations_df)
    """
    np.random.seed(42)
    
    # ==========================================
    # INVENTORY DATA
    # ==========================================
    num_products = 20
    
    product_names = [
        'Industrial Bearing Type A', 'Steel Plates Grade B', 'Hydraulic Pump Unit',
        'Electric Motor 5HP', 'Control Panel Assembly', 'Conveyor Belt Section',
        'Safety Valve Kit', 'Lubricant Premium Grade', 'Fastener Set M12',
        'Gasket Seal Pack', 'Pressure Sensor Digital', 'Cable Wire 10mm',
        'Junction Box IP67', 'Filter Cartridge HEPA', 'Coupling Flexible',
        'Switch Limit Type C', 'Relay Module 24V', 'Pneumatic Cylinder',
        'Solenoid Valve 2-way', 'Bearing Housing Unit'
    ]
    
    inventory_df = pd.DataFrame({
        'product_id': range(1, num_products + 1),
        'product_name': product_names,
        'current_stock': np.random.randint(30, 300, num_products),
        'safety_stock': np.random.randint(50, 100, num_products),
        'lead_time_days': np.random.randint(3, 14, num_products),
        'unit_cost': np.random.uniform(10, 500, num_products).round(2)
    })
    
    # ==========================================
    # MACHINE DATA
    # ==========================================
    num_machines = 10
    
    machines_df = pd.DataFrame({
        'machine_id': range(1, num_machines + 1),
        'machine_name': [f'Machine {i}' for i in range(1, num_machines + 1)],
        'temperature': np.random.uniform(65, 95, num_machines),
        'vibration': np.random.uniform(0.8, 4.5, num_machines),
        'operational_hours': np.random.randint(1000, 8000, num_machines),
        'last_maintenance': pd.date_range(end=datetime.now(), periods=num_machines, freq='45D')
    })
    
    # ==========================================
    # DEMAND HISTORY DATA
    # ==========================================
    dates = pd.date_range(end=datetime.now(), periods=180, freq='D')
    
    demand_records = []
    for product_id in range(1, num_products + 1):
        for date in dates:
            # Create realistic demand patterns
            base_demand = np.random.randint(5, 20)
            
            # Add weekly seasonality
            if date.dayofweek in [5, 6]:  # Weekend
                base_demand = int(base_demand * 0.6)
            
            # Add monthly trend
            month_factor = 1 + 0.1 * np.sin(date.day / 30 * 2 * np.pi)
            
            demand = int(base_demand * month_factor) + np.random.randint(-3, 4)
            demand = max(0, demand)
            
            demand_records.append({
                'date': date,
                'product_id': product_id,
                'demand': demand
            })
    
    demand_df = pd.DataFrame(demand_records)
    
    # ==========================================
    # OPERATIONS DATA
    # ==========================================
    operational_areas = [
        'Receiving Area',
        'Storage Zone A',
        'Storage Zone B',
        'Picking Area',
        'Packing Station',
        'Loading Area',
        'Quality Control',
        'Shipping Dock'
    ]
    
    operations_df = pd.DataFrame({
        'area': operational_areas,
        'utilization': np.random.uniform(60, 95, len(operational_areas)),
        'productivity_score': np.random.uniform(70, 95, len(operational_areas)),
        'downtime_hours': np.random.uniform(0.5, 3.5, len(operational_areas)),
        'efficiency_rate': np.random.uniform(75, 95, len(operational_areas)),
        'throughput': np.random.randint(100, 500, len(operational_areas))
    })
    
    return inventory_df, machines_df, demand_df, operations_df


def save_data(inventory_df, machines_df, demand_df, operations_df):
    """
    Save dataframes to CSV files
    
    Args:
        inventory_df: Inventory dataframe
        machines_df: Machines dataframe
        demand_df: Demand dataframe
        operations_df: Operations dataframe
    """
    import os
    
    # Create data directory if it doesn't exist
    os.makedirs('data', exist_ok=True)
    
    inventory_df.to_csv('data/inventory_data.csv', index=False)
    machines_df.to_csv('data/machinery_data.csv', index=False)
    demand_df.to_csv('data/demand_history.csv', index=False)
    operations_df.to_csv('data/operations_data.csv', index=False)


def preprocess_data(df, columns_to_normalize=None):
    """
    Preprocess data for ML models
    
    Args:
        df: Input dataframe
        columns_to_normalize: List of columns to normalize
        
    Returns:
        DataFrame: Preprocessed data
    """
    df_processed = df.copy()
    
    # Handle missing values
    df_processed = df_processed.fillna(method='ffill').fillna(method='bfill')
    
    # Normalize specified columns
    if columns_to_normalize:
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
        df_processed[columns_to_normalize] = scaler.fit_transform(df_processed[columns_to_normalize])
    
    return df_processed


def aggregate_metrics(df, group_by, agg_dict):
    """
    Aggregate metrics by specified grouping
    
    Args:
        df: Input dataframe
        group_by: Column(s) to group by
        agg_dict: Dictionary of aggregations
        
    Returns:
        DataFrame: Aggregated data
    """
    return df.groupby(group_by).agg(agg_dict).reset_index()


def detect_outliers(df, column, method='iqr', threshold=1.5):
    """
    Detect outliers in a column
    
    Args:
        df: Input dataframe
        column: Column name
        method: 'iqr' or 'zscore'
        threshold: Threshold value
        
    Returns:
        Series: Boolean series indicating outliers
    """
    if method == 'iqr':
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        
        lower_bound = Q1 - threshold * IQR
        upper_bound = Q3 + threshold * IQR
        
        return (df[column] < lower_bound) | (df[column] > upper_bound)
    
    elif method == 'zscore':
        from scipy import stats
        z_scores = np.abs(stats.zscore(df[column]))
        return z_scores > threshold
    
    return pd.Series([False] * len(df))


def create_time_features(df, date_column):
    """
    Create time-based features from date column
    
    Args:
        df: Input dataframe
        date_column: Name of date column
        
    Returns:
        DataFrame: Data with additional time features
    """
    df = df.copy()
    df[date_column] = pd.to_datetime(df[date_column])
    
    df['year'] = df[date_column].dt.year
    df['month'] = df[date_column].dt.month
    df['day'] = df[date_column].dt.day
    df['day_of_week'] = df[date_column].dt.dayofweek
    df['week_of_year'] = df[date_column].dt.isocalendar().week
    df['is_weekend'] = df['day_of_week'].isin([5, 6]).astype(int)
    df['is_month_start'] = df[date_column].dt.is_month_start.astype(int)
    df['is_month_end'] = df[date_column].dt.is_month_end.astype(int)
    
    return df


def calculate_rolling_statistics(df, column, windows=[7, 14, 30]):
    """
    Calculate rolling statistics for a column
    
    Args:
        df: Input dataframe
        column: Column name
        windows: List of window sizes
        
    Returns:
        DataFrame: Data with rolling statistics
    """
    df = df.copy()
    
    for window in windows:
        df[f'{column}_rolling_mean_{window}d'] = df[column].rolling(window=window).mean()
        df[f'{column}_rolling_std_{window}d'] = df[column].rolling(window=window).std()
        df[f'{column}_rolling_min_{window}d'] = df[column].rolling(window=window).min()
        df[f'{column}_rolling_max_{window}d'] = df[column].rolling(window=window).max()
    
    return df
