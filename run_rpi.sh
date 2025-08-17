#!/bin/bash
# Raspberry Pi Launcher for Daggerheart Tracker
# run_rpi.sh

echo "🎲 Starting Daggerheart Tracker for Raspberry Pi..."

# Set Raspberry Pi specific environment variables
export QT_QPA_PLATFORM=eglfs
export QT_QPA_EGLFS_FORCE888=1
export QT_QPA_EGLFS_WIDTH=800
export QT_QPA_EGLFS_HEIGHT=480

# Enable hardware acceleration
export QT_QPA_EGLFS_INTEGRATION=eglfs_kms

# Set font scaling for better readability on small screens
export QT_SCALE_FACTOR=1.0
export QT_FONT_DPI=96

# Force fullscreen for touchscreen
export QT_QPA_EGLFS_FORCE_FULLSCREEN=1

# Check if we're running on actual Raspberry Pi hardware
if grep -q "Raspberry Pi" /proc/cpuinfo; then
    echo "✅ Detected Raspberry Pi hardware"
    
    # Set optimal GPU memory split
    if [ -f /boot/config.txt ]; then
        if ! grep -q "gpu_mem=128" /boot/config.txt; then
            echo "⚠️  Consider adding 'gpu_mem=128' to /boot/config.txt for better performance"
        fi
    fi
    
    # Check for 7" touchscreen
    if [ -f /sys/class/backlight/rpi_backlight/brightness ]; then
        echo "📱 Detected official 7\" touchscreen"
    fi
else
    echo "💻 Running on non-Raspberry Pi system (development mode)"
    # Use windowed mode for development
    unset QT_QPA_EGLFS_FORCE_FULLSCREEN
    export QT_QPA_PLATFORM=xcb
fi

# Check Python and Qt installation
if ! command -v python3 &> /dev/null; then
    echo "❌ Python3 not found. Please install Python3."
    exit 1
fi

# Check if PySide6 is installed
python3 -c "import PySide6" 2>/dev/null
if [ $? -ne 0 ]; then
    echo "📦 Installing PySide6..."
    pip3 install PySide6 --user
fi

# Change to script directory
cd "$(dirname "$0")"

echo "🚀 Launching application..."
python3 main_qt.py

echo "✅ Application finished"
