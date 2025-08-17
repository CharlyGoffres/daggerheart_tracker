# main.py
"""
Main entry point for the Raspberry Pi Touchscreen App using Kivy.
Features:
- Main menu navigation
- Modular screens (tabs)
- Touch-friendly UI
- Settings management
- GPIO reading (mocked for non-RPi environments)
"""

import kivy
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from utils.settings import SettingsManager

from screens.menu import MenuScreen
from screens.settings import SettingsScreen
from screens.gpio import GPIOScreen
from screens.rolls import RollsScreen
from screens.characteristics import CharacteristicsScreen

# Set window size for testing (remove on real Pi)
Window.size = (800, 480)

class MainApp(App):
    def build(self):
        self.settings_manager = SettingsManager('settings.json')
        # Character data with ability modifiers
        self.character = {
            'Fuerza': 2,
            'Destreza': 1,
            'Carisma': 0,
            'Constitución': 1,
            'Sabiduría': 0,
            'Inteligencia': -1
        }
        self.sm = ScreenManager(transition=FadeTransition())
        self.sm.add_widget(MenuScreen(name='menu', app=self))
        self.sm.add_widget(SettingsScreen(name='settings', app=self))
        self.sm.add_widget(GPIOScreen(name='gpio', app=self))
        self.sm.add_widget(RollsScreen(name='rolls', app=self))
        self.sm.add_widget(CharacteristicsScreen(name='characteristics', app=self))
        return self.sm

    def switch_screen(self, screen_name):
        self.sm.current = screen_name

if __name__ == '__main__':
    MainApp().run()
