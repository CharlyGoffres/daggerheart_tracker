# Daggerheart Tracker - Qt/QML Version

## Migration from Kivy to PySide6/Qt

This is the new Qt/QML version of the Daggerheart Tracker, offering a more modern and native user experience.

### What's New in Qt Version

🚀 **Modern UI Framework**: Built with PySide6 and QML for native performance
🎨 **Beautiful Gradients**: Each screen has its own unique gradient background
📱 **Responsive Design**: Adapts to different screen sizes seamlessly
⚡ **Smooth Animations**: Hardware-accelerated animations and transitions
🔧 **Better Architecture**: Clean separation between UI and business logic
🎯 **Type Safety**: Strongly typed properties and signals

### Features

- **Beautiful Menu**: Modern card-based navigation with gradient backgrounds
- **Dice Rolling**: Animated dice rolls with advantage/disadvantage support
- **Character Management**: Real-time character sheet with property binding
- **Combat System**: Quick combat actions and resource management
- **Settings**: Comprehensive settings with instant persistence
- **Responsive Layout**: Works great on different screen sizes

### Installation

1. **Install PySide6**:
   ```bash
   # Run the installation script
   install_qt.bat
   
   # Or manually install
   pip install -r requirements_qt.txt
   ```

2. **Run the Application**:
   ```bash
   # Use the batch file
   run_qt.bat
   
   # Or run directly
   python main_qt.py
   ```

### Project Structure

```
├── main_qt.py              # Main Qt application entry point
├── qt_models/               # Qt-specific models and controllers
│   ├── character_model.py   # Character data with Qt properties
│   ├── dice_roller.py       # Dice rolling with Qt signals
│   └── settings_manager.py  # Settings with persistence
├── qml/                     # QML user interface files
│   ├── main.qml            # Main application window
│   ├── MenuScreen.qml      # Beautiful main menu
│   ├── RollsScreen.qml     # Dice rolling interface
│   ├── CharacterScreen.qml # Character sheet
│   ├── CombatScreen.qml    # Combat management
│   ├── SettingsScreen.qml  # Application settings
│   ├── BottomNavigation.qml # Navigation component
│   ├── MenuCard.qml        # Reusable menu card
│   └── ModernButton.qml    # Modern button component
└── requirements_qt.txt     # Qt dependencies
```

### Key Improvements Over Kivy Version

1. **Performance**: Native Qt rendering is faster and more efficient
2. **Look & Feel**: More modern and native appearance
3. **Animations**: Hardware-accelerated smooth animations
4. **Development**: Better debugging and development tools
5. **Maintenance**: Cleaner architecture and easier to extend
6. **Cross-platform**: Better support across Windows, macOS, and Linux

### Technical Architecture

- **Qt Models**: Business logic in Python with Qt properties
- **QML Views**: Declarative UI with beautiful styling
- **Signal/Slot System**: Clean communication between UI and logic
- **Property Binding**: Automatic UI updates when data changes
- **Component System**: Reusable UI components

### Screen-Specific Gradients

Each screen has its own beautiful gradient:
- **Menu**: Purple to blue gradient (#667eea → #764ba2)
- **Rolls**: Pink to light pink (#ff9a9e → #fecfef)
- **Character**: Aqua to pink (#a8edea → #fed6e3)
- **Combat**: Red to orange (#ff6b6b → #ffa726)
- **Settings**: Cream to peach (#ffecd2 → #fcb69f)

### Future Enhancements

- [ ] Advanced character creation wizard
- [ ] Spell and ability database
- [ ] Campaign management
- [ ] Network multiplayer support
- [ ] Custom dice and macros
- [ ] Audio feedback system
- [ ] Tablet-optimized layouts
- [ ] Character import/export

### Requirements

- Python 3.8+
- PySide6 6.5+
- Windows 10+ (recommended)

### Comparison: Kivy vs Qt

| Feature | Kivy | Qt/QML |
|---------|------|--------|
| Performance | Good | Excellent |
| Native Look | No | Yes |
| Animation | Basic | Advanced |
| Development | Complex | Intuitive |
| Debugging | Limited | Excellent |
| Documentation | Good | Excellent |
| Community | Small | Large |

The Qt version provides a more professional and maintainable codebase while delivering a superior user experience.
