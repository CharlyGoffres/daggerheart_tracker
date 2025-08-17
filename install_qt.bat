@echo off
echo Installing PySide6 for Daggerheart Tracker...
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH
    echo Please install Python 3.8+ from https://python.org
    pause
    exit /b 1
)

echo Python found. Installing PySide6...
pip install --upgrade pip
pip install -r requirements_qt.txt

if errorlevel 1 (
    echo.
    echo ERROR: Failed to install PySide6
    echo Please try running as administrator or check your internet connection
    pause
    exit /b 1
)

echo.
echo Installation completed successfully!
echo You can now run the Qt version with: python main_qt.py
echo.
pause
