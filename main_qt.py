#!/usr/bin/env python3
"""
Daggerheart Tracker - Qt/QML Version
Modern RPG companion app built with PySide6 and QML
"""

import sys
import os
from pathlib import Path
from PySide6.QtGui import QGuiApplication
from PySide6.QtQml import QQmlApplicationEngine, qmlRegisterType
from PySide6.QtCore import QObject, Signal, Slot, Property

# Add the project directory to Python path
sys.path.append(str(Path(__file__).parent))

from qt_models.character_model import CharacterModel
from qt_models.dice_roller import DiceRoller
from qt_models.settings_manager import SettingsManager

class DaggerheartApp(QObject):
    """Main application controller"""
    
    # Signals for QML
    screenChanged = Signal(str)
    
    def __init__(self):
        super().__init__()
        self._current_screen = "menu"
        
        # Initialize models
        self.character = CharacterModel()
        self.dice_roller = DiceRoller()
        self.settings = SettingsManager()
    
    @Property(str, notify=screenChanged)
    def currentScreen(self):
        return self._current_screen
    
    @currentScreen.setter
    def currentScreen(self, screen):
        if self._current_screen != screen:
            self._current_screen = screen
            self.screenChanged.emit(screen)
    
    @Slot(str)
    def switchScreen(self, screen_name):
        """Switch to a different screen"""
        self.currentScreen = screen_name
        print(f"Switched to screen: {screen_name}")
    
    @Slot()
    def exitApp(self):
        """Exit the application"""
        QGuiApplication.quit()

def main():
    app = QGuiApplication(sys.argv)
    app.setApplicationName("Daggerheart Tracker")
    app.setOrganizationName("DaggerheartStudio")
    
    # Create QML engine
    engine = QQmlApplicationEngine()
    
    # Register custom types
    qmlRegisterType(CharacterModel, 'DaggerheartModels', 1, 0, 'CharacterModel')
    qmlRegisterType(DiceRoller, 'DaggerheartModels', 1, 0, 'DiceRoller')
    qmlRegisterType(SettingsManager, 'DaggerheartModels', 1, 0, 'SettingsManager')
    
    # Create app instance
    daggerheart_app = DaggerheartApp()
    
    # Expose to QML
    engine.rootContext().setContextProperty("app", daggerheart_app)
    engine.rootContext().setContextProperty("character", daggerheart_app.character)
    engine.rootContext().setContextProperty("diceRoller", daggerheart_app.dice_roller)
    engine.rootContext().setContextProperty("settings", daggerheart_app.settings)
    
    # Load main QML file
    qml_file = Path(__file__).resolve().parent / "qml" / "main.qml"
    engine.load(qml_file)
    
    if not engine.rootObjects():
        return -1
    
    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
