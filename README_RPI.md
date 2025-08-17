# Daggerheart Tracker - Raspberry Pi Setup Guide

This guide will help you set up the Daggerheart Tracker on a Raspberry Pi with optimal performance and the dice icon in the navigation.

## Hardware Requirements

- Raspberry Pi 3B+ or newer (4GB+ RAM recommended)
- 7" touchscreen display (800x480) or HDMI display
- MicroSD card (16GB+ recommended)
- Optional: Physical buttons connected to GPIO pins

## Software Requirements

- Raspberry Pi OS (Bullseye or newer)
- Python 3.9+
- Kivy 2.3.0+

## Installation

### 1. Update your Raspberry Pi

```bash
sudo apt update
sudo apt upgrade -y
```

### 2. Install system dependencies

```bash
sudo apt install -y python3-pip python3-venv
sudo apt install -y libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev
sudo apt install -y pkg-config libgl1-mesa-dev libgles2-mesa-dev
sudo apt install -y python3-setuptools libgstreamer1.0-dev git-core
sudo apt install -y gstreamer1.0-plugins-{bad,base,good,ugly}
sudo apt install -y gstreamer1.0-{omx,alsa} python3-dev libmtdev-dev
sudo apt install -y xclip xsel libjpeg-dev
```

### 3. Clone the repository

```bash
git clone <repository-url>
cd daggerheart_trackers
```

### 4. Set up Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements_rpi.txt
```

### 5. Configure display (for 7" touchscreen)

Edit `/boot/config.txt`:

```bash
sudo nano /boot/config.txt
```

Add these lines:

```
# Enable 7" touchscreen
dtoverlay=vc4-kms-v3d
max_framebuffers=2
gpu_mem=128

# Touchscreen calibration
dtoverlay=rpi-display,rotate=180
```

### 6. Run the application

```bash
# Make the startup script executable
chmod +x run_rpi.sh

# Run the application
./run_rpi.sh
```

## Features Optimized for Raspberry Pi

### 🎲 Dice Icon Navigation
- The rolls screen now features a proper dice icon (⚀⚁) in the bottom navigation
- Unicode symbols are used for better compatibility on Raspberry Pi

### Touch-Friendly Interface
- Minimum 60px touch targets for all buttons
- Optimized spacing and padding for finger navigation
- Larger fonts and icons for better visibility

### Performance Optimizations
- Faster animations (0.15s duration)
- Reduced graphics complexity
- Optimized for 800x480 displays
- Hardware acceleration when available

### Responsive Design
- Automatic detection of Raspberry Pi hardware
- Adaptive layout for different screen sizes
- Special handling for small touchscreens (3.5", 5", 7")

## Screen Layouts

### Supported Resolutions
- **7" Official Touchscreen**: 800x480 (primary target)
- **5" HDMI Display**: 800x480
- **3.5" Touchscreen**: 480x320
- **Custom displays**: Automatically adapts

### Navigation Icons
- 🏠 **Menú**: Main menu
- **⚀⚁ Dados**: Dice rolling (with dice icon!)
- **⚔ Personaje**: Character sheet
- **⚡ Combate**: Combat tracker
- **⚙ Ajustes**: Settings

## Troubleshooting

### Touch not working
```bash
# Check if touchscreen is detected
ls /dev/input/event*

# Calibrate touchscreen
sudo apt install xinput-calibrator
xinput_calibrator
```

### Performance issues
```bash
# Check GPU memory
vcgencmd get_mem gpu

# Increase GPU memory (in /boot/config.txt)
gpu_mem=128
```

### Application won't start
```bash
# Check Python version
python3 --version

# Check Kivy installation
python3 -c "import kivy; print(kivy.__version__)"

# Run with debug output
python3 main.py --debug
```

## GPIO Integration (Optional)

You can connect physical buttons to GPIO pins for hardware controls:

```python
# Example GPIO button mapping
BUTTONS = {
    'roll': 18,      # GPIO 18 for quick roll
    'menu': 19,      # GPIO 19 for menu
    'combat': 20,    # GPIO 20 for combat mode
}
```

## Autostart on Boot

To start the application automatically:

```bash
# Create systemd service
sudo nano /etc/systemd/system/daggerheart.service
```

```ini
[Unit]
Description=Daggerheart Tracker
After=graphical-session.target

[Service]
Type=simple
User=pi
WorkingDirectory=/home/pi/daggerheart_trackers
ExecStart=/home/pi/daggerheart_trackers/run_rpi.sh
Restart=always

[Install]
WantedBy=graphical-session.target
```

```bash
# Enable and start service
sudo systemctl enable daggerheart.service
sudo systemctl start daggerheart.service
```

## Development Tips

### Testing without Raspberry Pi
The application will automatically detect when it's not running on Raspberry Pi hardware and use appropriate fallbacks.

### Customizing for your display
Edit `components/platform_config.py` to add your custom display resolution:

```python
RPI_BREAKPOINTS = {
    'my_display': (1024, 600),  # Your custom resolution
}
```

## Performance Tips

1. **GPU Memory**: Allocate at least 128MB to GPU
2. **Overclocking**: Safe overclock can improve performance
3. **Heat Management**: Ensure adequate cooling
4. **SD Card**: Use high-speed cards (Class 10+ or better)

Enjoy your optimized Daggerheart Tracker on Raspberry Pi! 🎲
