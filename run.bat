@echo off
echo ============================================
echo   WarehouseMind - AI Industrial Platform   
echo ============================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo Error: Python is not installed
    echo Please install Python 3.10+ from https://www.python.org/downloads/
    pause
    exit /b 1
)

REM Check if requirements are installed
echo Checking dependencies...
python -c "import streamlit" >nul 2>&1
if errorlevel 1 (
    echo Installing requirements...
    pip install -r requirements.txt
)

echo.
echo Starting WarehouseMind...
echo The application will open in your browser automatically
echo.
echo If it doesn't open, visit: http://localhost:8501
echo.
echo Press Ctrl+C to stop the application
echo.

REM Run the application
streamlit run app.py
