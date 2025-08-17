"""
Settings Manager for Qt/QML Version
Manages application settings with persistence
"""

import json
from pathlib import Path
from PySide6.QtCore import QObject, Signal, Slot, Property

class SettingsManager(QObject):
    """Settings management with Qt properties"""
    
    # Signals
    darkThemeChanged = Signal()
    soundsEnabledChanged = Signal()
    animationsEnabledChanged = Signal()
    autoSaveChanged = Signal()
    diceSpeedChanged = Signal()
    
    def __init__(self):
        super().__init__()
        
        # Default settings
        self._dark_theme = True
        self._sounds_enabled = True
        self._animations_enabled = True
        self._auto_save = True
        self._dice_speed = 50
        
        # Settings file path
        self._settings_file = Path.home() / ".daggerheart_settings.json"
        
        # Load settings
        self.loadSettings()
    
    # Dark theme property
    @Property(bool, notify=darkThemeChanged)
    def darkTheme(self):
        return self._dark_theme
    
    @darkTheme.setter
    def darkTheme(self, value):
        if self._dark_theme != value:
            self._dark_theme = value
            self.darkThemeChanged.emit()
            self.saveSettings()
    
    # Sounds enabled property
    @Property(bool, notify=soundsEnabledChanged)
    def soundsEnabled(self):
        return self._sounds_enabled
    
    @soundsEnabled.setter
    def soundsEnabled(self, value):
        if self._sounds_enabled != value:
            self._sounds_enabled = value
            self.soundsEnabledChanged.emit()
            self.saveSettings()
    
    # Animations enabled property
    @Property(bool, notify=animationsEnabledChanged)
    def animationsEnabled(self):
        return self._animations_enabled
    
    @animationsEnabled.setter
    def animationsEnabled(self, value):
        if self._animations_enabled != value:
            self._animations_enabled = value
            self.animationsEnabledChanged.emit()
            self.saveSettings()
    
    # Auto save property
    @Property(bool, notify=autoSaveChanged)
    def autoSave(self):
        return self._auto_save
    
    @autoSave.setter
    def autoSave(self, value):
        if self._auto_save != value:
            self._auto_save = value
            self.autoSaveChanged.emit()
            self.saveSettings()
    
    # Dice speed property
    @Property(int, notify=diceSpeedChanged)
    def diceSpeed(self):
        return self._dice_speed
    
    @diceSpeed.setter
    def diceSpeed(self, value):
        if self._dice_speed != value:
            self._dice_speed = value
            self.diceSpeedChanged.emit()
            self.saveSettings()
    
    @Slot()
    def saveSettings(self):
        """Save settings to file"""
        try:
            settings_data = {
                "dark_theme": self._dark_theme,
                "sounds_enabled": self._sounds_enabled,
                "animations_enabled": self._animations_enabled,
                "auto_save": self._auto_save,
                "dice_speed": self._dice_speed
            }
            
            with open(self._settings_file, 'w') as f:
                json.dump(settings_data, f, indent=2)
        
        except Exception as e:
            print(f"Error saving settings: {e}")
    
    @Slot()
    def loadSettings(self):
        """Load settings from file"""
        try:
            if self._settings_file.exists():
                with open(self._settings_file, 'r') as f:
                    settings_data = json.load(f)
                
                self._dark_theme = settings_data.get("dark_theme", True)
                self._sounds_enabled = settings_data.get("sounds_enabled", True)
                self._animations_enabled = settings_data.get("animations_enabled", True)
                self._auto_save = settings_data.get("auto_save", True)
                self._dice_speed = settings_data.get("dice_speed", 50)
                
                # Emit all change signals
                self.darkThemeChanged.emit()
                self.soundsEnabledChanged.emit()
                self.animationsEnabledChanged.emit()
                self.autoSaveChanged.emit()
                self.diceSpeedChanged.emit()
        
        except Exception as e:
            print(f"Error loading settings: {e}")
    
    @Slot()
    def resetSettings(self):
        """Reset all settings to defaults"""
        self.darkTheme = True
        self.soundsEnabled = True
        self.animationsEnabled = True
        self.autoSave = True
        self.diceSpeed = 50
