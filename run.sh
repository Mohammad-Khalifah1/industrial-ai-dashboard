#!/bin/bash

echo "============================================"
echo "  WarehouseMind - AI Industrial Platform   "
echo "============================================"
echo ""

# Check if Python is installed
if ! command -v python3 &> /dev/null
then
    echo "Error: Python 3 is not installed"
    echo "Please install Python 3.10+ from https://www.python.org/downloads/"
    exit 1
fi

# Check if requirements are installed
echo "Checking dependencies..."
python3 -c "import streamlit" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "Installing requirements..."
    pip install -r requirements.txt
fi

echo ""
echo "Starting WarehouseMind..."
echo "The application will open in your browser automatically"
echo ""
echo "If it doesn't open, visit: http://localhost:8501"
echo ""
echo "Press Ctrl+C to stop the application"
echo ""

# Run the application
streamlit run app.py
