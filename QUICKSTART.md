# WarehouseMind Quick Start Guide

## Installation (3 Minutes)

1. **Install Python 3.10+**
   Download from: https://www.python.org/downloads/

2. **Open Terminal/Command Prompt**

3. **Navigate to Project Folder**
   ```bash
   cd path/to/warehousemind
   ```

4. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**
   ```bash
   streamlit run app.py
   ```

6. **Access in Browser**
   - Automatically opens at http://localhost:8501
   - If not, manually visit the URL shown in terminal

## First Time Use

The application will automatically:
- Generate demo data (20 products, 10 machines, 180 days of demand history)
- Train AI models
- Display the Executive Overview dashboard

## Navigation

Use the sidebar to navigate between pages:
- **Executive Overview**: Main dashboard with overall metrics
- **Smart Inventory**: Demand forecasting and stock management
- **Predictive Maintenance**: Machine health and failure prediction
- **Operations Optimization**: Bottleneck detection and efficiency
- **AI Decision Center**: Generate AI recommendations

## Key Actions

### Generate AI Recommendations
1. Go to "AI Decision Center"
2. Click "Generate AI Operational Recommendations"
3. Wait 2 seconds for analysis
4. Review prioritized recommendations
5. Download CSV report if needed

### View Machine Health
1. Go to "Predictive Maintenance"
2. Select a machine from dropdown
3. View health gauge and failure probability
4. Check temperature/vibration trends
5. Review RUL estimation and recommendations

### Forecast Demand
1. Go to "Smart Inventory"
2. Select a product from dropdown
3. View 14-day demand forecast
4. Check confidence intervals
5. Review reorder recommendations

## Understanding the Dashboard

### Health Scores
- **75-100%**: Green - Healthy
- **50-75%**: Yellow - Warning
- **0-50%**: Red - Critical

### Risk Levels
- **0-30%**: Stable
- **30-60%**: Medium Risk
- **60-100%**: Critical

### Priorities
- **Priority 1**: Critical - Immediate action required
- **Priority 2**: High - Action within days
- **Priority 3**: Medium - Plan for implementation

## Troubleshooting

### Application won't start
```bash
# Try different port
streamlit run app.py --server.port 8502
```

### Missing modules
```bash
# Reinstall all requirements
pip install -r requirements.txt --force-reinstall
```

### No data showing
- Application generates demo data automatically
- Check terminal for error messages
- Restart the application

## Next Steps

1. Explore all 5 pages
2. Try different products/machines in dropdowns
3. Generate AI recommendations
4. Customize thresholds in code if needed
5. Replace demo data with your actual data

## Support

- Read the full README.md for detailed documentation
- Check AI Models section for technical details
- Review code comments for customization options

---

**Tips:**
- Let the app load completely before clicking buttons
- Use the sidebar status to see current risk level
- Generate recommendations after exploring other pages
- Download CSV reports for record keeping

**Enjoy WarehouseMind!**
