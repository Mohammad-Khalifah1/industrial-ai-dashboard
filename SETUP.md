# WarehouseMind - Complete Setup Instructions

## Project Structure

After downloading all files, organize them in this structure:

```
warehousemind/
│
├── app.py                          # Main application
├── requirements.txt                # Dependencies
├── README.md                       # Full documentation
├── QUICKSTART.md                   # Quick start guide
├── PRESENTATION_GUIDE.md           # Presentation tips
├── run.sh                          # Linux/Mac startup script
├── run.bat                         # Windows startup script
│
├── models/
│   ├── __init__.py                # Empty file (create manually)
│   ├── maintenance_models.py
│   ├── demand_forecasting.py
│   └── decision_engine.py
│
└── utils/
    ├── __init__.py                # Empty file (create manually)
    ├── data_processing.py
    ├── calculations.py
    └── visualizations.py
```

## Installation Steps

### Option 1: Quick Start (Recommended)

**Windows:**
1. Double-click `run.bat`
2. Wait for installation to complete
3. Browser will open automatically

**Mac/Linux:**
1. Open Terminal
2. Navigate to project folder: `cd path/to/warehousemind`
3. Run: `bash run.sh`
4. Browser will open automatically

### Option 2: Manual Installation

1. **Install Python 3.10+**
   - Download from: https://www.python.org/downloads/
   - During installation, check "Add Python to PATH"

2. **Open Terminal/Command Prompt**

3. **Navigate to Project Folder**
   ```bash
   cd path/to/warehousemind
   ```

4. **Create Virtual Environment (Optional but Recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Mac/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

5. **Install Requirements**
   ```bash
   pip install -r requirements.txt
   ```

6. **Run Application**
   ```bash
   streamlit run app.py
   ```

7. **Access in Browser**
   - Visit: http://localhost:8501
   - Or use the URL shown in terminal

## Important Notes

### Creating __init__.py Files

If the models and utils folders don't have __init__.py files, create them:

**Windows:**
```bash
type nul > models\__init__.py
type nul > utils\__init__.py
```

**Mac/Linux:**
```bash
touch models/__init__.py
touch utils/__init__.py
```

Or simply create empty text files named `__init__.py` in each folder.

### Data Files

The application automatically generates demo data on first run. No need to create data files manually.

### Common Installation Issues

**Issue: "pip is not recognized"**
Solution: Reinstall Python and check "Add Python to PATH"

**Issue: "Module not found: streamlit"**
Solution: Run `pip install -r requirements.txt` again

**Issue: "Port 8501 is already in use"**
Solution: Run `streamlit run app.py --server.port 8502`

**Issue: Application runs but shows errors**
Solution: Make sure __init__.py files exist in models/ and utils/

## First Run

On first run, the application will:
1. Generate demo data (takes ~2 seconds)
2. Initialize AI models
3. Display Executive Overview dashboard

You'll see:
- 20 products in inventory
- 10 machines being monitored
- 180 days of historical demand data
- 8 operational areas

## Testing the Platform

### 5-Minute Quick Test
1. Check Executive Overview dashboard
2. Go to AI Decision Center
3. Click "Generate AI Operational Recommendations"
4. Review the recommendations

### Full Test (15 minutes)
1. Executive Overview - Review all metrics
2. Smart Inventory - Select a product and view forecast
3. Predictive Maintenance - Select a machine and check health
4. Operations Optimization - Review bottlenecks
5. AI Decision Center - Generate recommendations

## Customization

### Change Port Number
```bash
streamlit run app.py --server.port YOUR_PORT
```

### Run in Background
```bash
# Linux/Mac
nohup streamlit run app.py &

# Windows - use a service wrapper
```

### Access from Other Devices
```bash
streamlit run app.py --server.address 0.0.0.0
```
Then access via: http://YOUR_IP:8501

## File Descriptions

**Core Files:**
- `app.py` - Main Streamlit application (800+ lines)
- `requirements.txt` - All Python dependencies

**Documentation:**
- `README.md` - Complete documentation
- `QUICKSTART.md` - Quick start guide
- `PRESENTATION_GUIDE.md` - How to present/demo

**Models (AI/ML):**
- `maintenance_models.py` - Predictive maintenance ML
- `demand_forecasting.py` - Inventory forecasting
- `decision_engine.py` - Recommendation system

**Utilities:**
- `data_processing.py` - Data loading and generation
- `calculations.py` - Business logic and KPIs
- `visualizations.py` - Chart creation functions

**Scripts:**
- `run.sh` - Linux/Mac startup script
- `run.bat` - Windows startup script

## Next Steps

1. Read QUICKSTART.md for basic usage
2. Explore all 5 pages in the application
3. Read PRESENTATION_GUIDE.md if presenting
4. Check README.md for detailed technical info
5. Customize thresholds and parameters as needed

## Support & Documentation

- **Quick Help**: QUICKSTART.md
- **Full Docs**: README.md
- **Presentation**: PRESENTATION_GUIDE.md
- **Code Comments**: Check Python files

## Success Checklist

- [ ] Python 3.10+ installed
- [ ] All files in correct folder structure
- [ ] __init__.py files in models/ and utils/
- [ ] Requirements installed
- [ ] Application runs without errors
- [ ] Can access http://localhost:8501
- [ ] Executive Overview loads with data
- [ ] Can generate AI recommendations

## Troubleshooting Resources

1. Check terminal/console for error messages
2. Verify folder structure matches above
3. Ensure __init__.py files exist
4. Try reinstalling requirements
5. Restart the application
6. Try a different port number

---

**You're all set! Run the application and explore WarehouseMind.**

For detailed usage, see QUICKSTART.md
For presentation tips, see PRESENTATION_GUIDE.md
For technical details, see README.md

**Enjoy WarehouseMind!**
