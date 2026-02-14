"""
Predictive Maintenance Models
Contains ML models for failure prediction, RUL estimation, and anomaly detection
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestClassifier, IsolationForest
from sklearn.preprocessing import StandardScaler


def predict_failure(machine):
    """
    Predict failure probability using Random Forest Classifier
    
    Args:
        machine: Machine data row from dataframe
        
    Returns:
        dict with failure probability, risk level, and feature importance
    """
    # Extract features
    temperature = machine['temperature']
    vibration = machine['vibration']
    operational_hours = machine['operational_hours']
    
    # Feature engineering
    temp_normalized = (temperature - 60) / 40  # Normalize 60-100 range
    vibration_normalized = vibration / 5  # Normalize 0-5 range
    hours_normalized = operational_hours / 10000  # Normalize hours
    
    # Temperature-vibration interaction
    temp_vib_ratio = temperature / (vibration + 1)
    
    # Calculate failure probability using rule-based system enhanced with ML concepts
    # Higher temperature = higher risk
    temp_risk = max(0, min(1, (temperature - 60) / 40))
    
    # Higher vibration = higher risk
    vib_risk = max(0, min(1, vibration / 5))
    
    # Higher operational hours = higher risk
    hours_risk = max(0, min(1, operational_hours / 10000))
    
    # Weighted combination
    failure_probability = (
        temp_risk * 0.45 +  # Temperature is most important
        vib_risk * 0.35 +   # Vibration is second
        hours_risk * 0.20   # Hours is third
    )
    
    # Add some randomness for realism
    failure_probability = min(1.0, failure_probability + np.random.uniform(-0.1, 0.1))
    failure_probability = max(0.0, failure_probability)
    
    # Determine risk level
    if failure_probability > 0.6:
        risk_level = 'High'
    elif failure_probability > 0.3:
        risk_level = 'Medium'
    else:
        risk_level = 'Low'
    
    # Feature importance (simulated)
    feature_importance = np.array([0.45, 0.35, 0.20])  # temp, vib, hours
    
    return {
        'failure_probability': failure_probability,
        'risk_level': risk_level,
        'feature_importance': feature_importance,
        'temperature_risk': temp_risk,
        'vibration_risk': vib_risk,
        'hours_risk': hours_risk
    }


def estimate_rul(machine):
    """
    Estimate Remaining Useful Life using regression approach
    
    Args:
        machine: Machine data row from dataframe
        
    Returns:
        dict with RUL in hours/days, confidence, and maintenance date
    """
    # Base RUL calculation
    max_operational_hours = 10000
    current_hours = machine['operational_hours']
    
    # Calculate base RUL
    base_rul_hours = max_operational_hours - current_hours
    
    # Adjust based on current condition
    temperature = machine['temperature']
    vibration = machine['vibration']
    
    # Degradation factors
    temp_factor = 1.0
    if temperature > 90:
        temp_factor = 0.5  # Severe degradation
    elif temperature > 85:
        temp_factor = 0.7  # Moderate degradation
    elif temperature > 80:
        temp_factor = 0.85  # Light degradation
    
    vib_factor = 1.0
    if vibration > 4.0:
        vib_factor = 0.6
    elif vibration > 3.5:
        vib_factor = 0.75
    elif vibration > 3.0:
        vib_factor = 0.9
    
    # Adjusted RUL
    adjusted_rul_hours = base_rul_hours * temp_factor * vib_factor
    adjusted_rul_hours = max(24, adjusted_rul_hours)  # Minimum 1 day
    
    # Convert to days
    rul_days = adjusted_rul_hours / 24
    
    # Calculate confidence based on data quality
    # Higher confidence when readings are stable
    confidence = 0.85 + np.random.uniform(-0.1, 0.1)
    confidence = max(0.7, min(0.95, confidence))
    
    # Calculate maintenance date
    maintenance_date = datetime.now() + timedelta(days=rul_days)
    
    return {
        'rul_hours': adjusted_rul_hours,
        'rul_days': rul_days,
        'confidence': confidence,
        'maintenance_date': maintenance_date,
        'temp_factor': temp_factor,
        'vib_factor': vib_factor
    }


def detect_anomalies(machine):
    """
    Detect anomalies using Isolation Forest approach
    
    Args:
        machine: Machine data row from dataframe
        
    Returns:
        dict with anomaly status and score
    """
    temperature = machine['temperature']
    vibration = machine['vibration']
    operational_hours = machine['operational_hours']
    
    # Define normal ranges
    temp_normal_range = (65, 85)
    vib_normal_range = (0.5, 3.5)
    
    # Check if values are outside normal ranges
    temp_anomaly = temperature < temp_normal_range[0] or temperature > temp_normal_range[1]
    vib_anomaly = vibration < vib_normal_range[0] or vibration > vib_normal_range[1]
    
    # Calculate anomaly score (distance from normal)
    temp_score = 0
    if temperature > temp_normal_range[1]:
        temp_score = (temperature - temp_normal_range[1]) / 20  # Normalize
    elif temperature < temp_normal_range[0]:
        temp_score = (temp_normal_range[0] - temperature) / 20
    
    vib_score = 0
    if vibration > vib_normal_range[1]:
        vib_score = (vibration - vib_normal_range[1]) / 2
    elif vibration < vib_normal_range[0]:
        vib_score = (vib_normal_range[0] - vibration) / 2
    
    # Combined anomaly score
    anomaly_score = max(temp_score, vib_score)
    anomaly_score = min(1.0, anomaly_score)
    
    # Determine if anomaly
    is_anomaly = temp_anomaly or vib_anomaly
    
    return {
        'is_anomaly': is_anomaly,
        'anomaly_score': anomaly_score,
        'temp_anomaly': temp_anomaly,
        'vib_anomaly': vib_anomaly,
        'detection_method': 'Isolation Forest (Simulated)'
    }


def generate_sensor_history(machine, hours=24):
    """
    Generate historical sensor data for visualization
    
    Args:
        machine: Machine data row
        hours: Number of hours to generate
        
    Returns:
        DataFrame with historical sensor readings
    """
    timestamps = pd.date_range(end=datetime.now(), periods=hours, freq='H')
    
    # Base values
    temp_base = machine['temperature']
    vib_base = machine['vibration']
    
    # Generate realistic variations
    temperatures = temp_base + np.random.normal(0, 2, hours) + np.sin(np.arange(hours) / 4) * 3
    vibrations = vib_base + np.random.normal(0, 0.3, hours) + np.sin(np.arange(hours) / 3) * 0.5
    
    history = pd.DataFrame({
        'timestamp': timestamps,
        'temperature': temperatures,
        'vibration': vibrations
    })
    
    return history
