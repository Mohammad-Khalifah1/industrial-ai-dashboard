# WarehouseMind - AI-Powered Industrial Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.29.0-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

**An enterprise-grade AI decision intelligence platform for industrial warehouse management**

[Features](#features) • [Installation](#installation) • [Usage](#usage) • [AI Models](#ai-models) • [Architecture](#architecture)

---

## Overview

WarehouseMind is not just a data dashboard - it's a comprehensive **Decision Intelligence Platform** that transforms operational data into actionable insights using advanced machine learning algorithms. The platform integrates inventory management, predictive maintenance, and operations optimization into a unified system that helps warehouse managers make data-driven decisions.

### Why WarehouseMind?

- **Reduce Costs**: Prevent equipment failures and optimize inventory levels
- **Increase Efficiency**: Identify and eliminate operational bottlenecks
- **Data-Driven Decisions**: AI-powered recommendations backed by predictive analytics
- **Proactive Management**: Predict issues before they become critical

---

## Features

### 1. Executive Overview Dashboard
- Real-time warehouse risk assessment
- Machine health monitoring
- Inventory health scoring
- Predicted monthly savings
- Active alerts tracking
- Multi-dimensional trend analysis
- AI operational insights panel

### 2. Smart Inventory Management
- AI-powered demand forecasting (ARIMA, Prophet, Gradient Boosting)
- Automated reorder recommendations
- Safety stock optimization
- Stock status heatmap visualization
- Low stock alerts
- Overstock detection
- Inventory turnover analysis

### 3. Predictive Maintenance Module
- Failure probability prediction (Random Forest, XGBoost)
- Remaining Useful Life (RUL) estimation
- Anomaly detection (Isolation Forest)
- Temperature and vibration monitoring
- Real-time sensor trend analysis
- Maintenance scheduling recommendations
- Parts requirement forecasting

### 4. Operations Optimization
- Resource utilization tracking
- Bottleneck detection (K-Means Clustering)
- Productivity scoring
- Downtime analysis (Pareto charts)
- Efficiency rate monitoring
- Workforce optimization recommendations

### 5. AI Decision Center
- Multi-criteria decision engine
- Prioritized action recommendations
- Risk-weighted scoring model
- ROI calculation for recommendations
- Implementation timeline planning
- Comprehensive decision reports

---

## AI & Machine Learning Techniques

### Demand Forecasting
- **ARIMA** (AutoRegressive Integrated Moving Average)
- **Facebook Prophet** for seasonality detection
- **Gradient Boosting Regressor** for feature-based prediction
- Time series feature engineering
- Trend and seasonality modeling
- Confidence interval estimation

### Predictive Maintenance
- **Random Forest Classifier** for failure prediction
- **Random Forest Regressor** for RUL estimation
- **Isolation Forest** for anomaly detection
- **XGBoost** for advanced predictions
- Time-series feature extraction
- Condition-based monitoring

### Inventory Optimization
- Economic Order Quantity (EOQ) calculation
- Safety stock modeling
- Reorder point optimization
- ABC analysis
- Demand pattern recognition
- Turnover ratio analysis

### Operations Intelligence
- **K-Means Clustering** for pattern detection
- Bottleneck identification algorithms
- Resource utilization optimization
- Pareto analysis
- Efficiency scoring

### Decision Engine
- Multi-criteria decision logic
- Rule-based AI system
- Weighted risk scoring
- Data-driven operational intelligence
- ROI-based prioritization

---

## Installation

### Prerequisites
- Python 3.10 or higher
- pip package manager
- 4GB+ RAM recommended
- Modern web browser

### Step-by-Step Installation

1. **Clone the Repository**
```bash
git clone https://github.com/yourusername/warehousemind.git
cd warehousemind
```

2. **Create Virtual Environment** (Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. **Install Dependencies**
```bash
pip install -r requirements.txt
```

4. **Verify Installation**
```bash
python -c "import streamlit; print(streamlit.__version__)"
```

---

## Usage

### Starting the Application

1. **Navigate to Project Directory**
```bash
cd warehousemind
```

2. **Launch Streamlit App**
```bash
streamlit run app.py
```

3. **Access the Application**
- Default URL: `http://localhost:8501`
- The app will automatically open in your browser
- Network URL displayed in terminal for remote access

### Using the Platform

#### Executive Overview
- View overall system health and risk levels
- Monitor key performance indicators
- Explore interactive 3D visualizations
- Review AI-generated operational insights

#### Smart Inventory
- Select products for demand forecasting
- View stock status heatmap
- Review low stock alerts
- Get AI reorder recommendations

#### Predictive Maintenance
- Select machines for detailed analysis
- Monitor health scores and failure probability
- View sensor trend charts
- Review RUL estimates
- Get maintenance recommendations

#### Operations Optimization
- Analyze resource utilization by area
- Identify bottlenecks
- Review downtime causes
- Get optimization suggestions

#### AI Decision Center
- Click "Generate AI Recommendations"
- Review prioritized action items
- Export decision reports
- Track implementation timelines

---

## Project Structure

```
warehousemind/
│
├── app.py                          # Main Streamlit application
├── requirements.txt                # Python dependencies
├── README.md                       # Project documentation
│
├── models/
│   ├── maintenance_models.py       # Predictive maintenance ML
│   ├── demand_forecasting.py       # Inventory forecasting
│   └── decision_engine.py          # AI recommendation system
│
├── utils/
│   ├── data_processing.py          # Data preprocessing
│   ├── calculations.py             # Business logic
│   └── visualizations.py           # Chart functions
│
└── data/                           # Data directory (auto-generated)
    ├── inventory_data.csv
    ├── machinery_data.csv
    ├── demand_history.csv
    └── operations_data.csv
```

---

## Key Metrics & KPIs

### Machine Health
- **Health Score**: 0-100% based on temperature, vibration, operational hours
- **Failure Probability**: Likelihood of failure in next 7 days
- **RUL**: Remaining operational hours before maintenance required

### Inventory Health
- **Stock Adequacy**: % of products above safety stock
- **Turnover Rate**: Annual inventory turnover ratio
- **Days of Inventory**: Average days of stock on hand
- **Fill Rate**: % of demand fulfilled without stockout

### Operational Efficiency
- **Resource Utilization**: % of capacity being used
- **Productivity Score**: 0-100 based on throughput
- **Downtime Hours**: Weekly unplanned downtime
- **Efficiency Rate**: Actual vs. target performance

---

## Data Format

### Inventory Data
```csv
product_id,product_name,current_stock,safety_stock,lead_time_days,unit_cost
1,Industrial Bearing Type A,150,50,7,125.50
```

### Machine Data
```csv
machine_id,machine_name,temperature,vibration,operational_hours,last_maintenance
1,Machine 1,82.5,2.3,4500,2025-12-15
```

### Demand History
```csv
date,product_id,demand
2026-01-01,1,145
```

### Operations Data
```csv
area,utilization,productivity_score,downtime_hours,efficiency_rate,throughput
Receiving Area,85.2,88,1.5,92.3,350
```

---

## Technical Architecture

### Frontend
- **Streamlit**: Interactive web framework
- **Plotly**: Interactive 3D visualizations
- **Custom CSS**: Industrial-themed dark mode UI

### Backend
- **Pandas**: Data manipulation
- **NumPy**: Numerical computing
- **Scikit-learn**: Machine learning models
- **SciPy**: Statistical functions

### ML Pipeline
1. Data ingestion and preprocessing
2. Feature engineering
3. Model training (offline)
4. Real-time prediction
5. Decision generation
6. Visualization

---

## Customization

### Adding New Products
Edit `data/inventory_data.csv` or use the demo data generator

### Adjusting Thresholds
Modify thresholds in `utils/calculations.py`:
```python
# Temperature thresholds
TEMP_WARNING = 80  # °C
TEMP_CRITICAL = 85  # °C

# Utilization thresholds
UTIL_WARNING = 75  # %
UTIL_CRITICAL = 85  # %
```

### Custom ML Models
Replace model implementations in `models/` directory while maintaining the same interface

---

## Performance Optimization

### For Large Datasets
- Use data sampling for visualizations
- Implement caching with `@st.cache_data`
- Consider database backend instead of CSV

### For Multiple Users
- Deploy on cloud platform (AWS, GCP, Azure)
- Use load balancer
- Implement authentication

---

## Troubleshooting

### Common Issues

**Port already in use:**
```bash
streamlit run app.py --server.port 8502
```

**Module not found:**
```bash
pip install -r requirements.txt --force-reinstall
```

**Data not loading:**
- Check that demo data is being generated
- Verify file paths in `utils/data_processing.py`

**Slow performance:**
- Reduce dataset size for testing
- Close other applications
- Increase system RAM allocation

---

## Deployment

### Local Network
```bash
streamlit run app.py --server.address 0.0.0.0
```

### Cloud Deployment (Streamlit Cloud)
1. Push code to GitHub
2. Visit [share.streamlit.io](https://share.streamlit.io)
3. Connect repository
4. Deploy

### Docker Deployment
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["streamlit", "run", "app.py"]
```

---

## Future Enhancements

- [ ] Real-time data integration (IoT sensors)
- [ ] Mobile responsive design
- [ ] Multi-warehouse support
- [ ] Advanced LSTM models for time series
- [ ] Automated report scheduling
- [ ] Email/SMS alert system
- [ ] API for third-party integration
- [ ] User authentication and roles
- [ ] Historical data comparison
- [ ] What-if scenario analysis

---

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit changes (`git commit -m 'Add AmazingFeature'`)
4. Push to branch (`git push origin feature/AmazingFeature`)
5. Open Pull Request

---

## License

This project is licensed under the MIT License.

```
MIT License

Copyright (c) 2026 WarehouseMind

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```

---

## Acknowledgments

- Streamlit team for the amazing framework
- Scikit-learn contributors for ML tools
- Plotly team for interactive visualizations
- Open-source community

---

## Contact

**Project Link**: [https://github.com/yourusername/warehousemind](https://github.com/yourusername/warehousemind)

---

<div align="center">

**Made with AI & Data Science**

*WarehouseMind v1.0 - Transform your warehouse operations with AI*

</div>
