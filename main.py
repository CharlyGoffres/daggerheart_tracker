# main.py
"""
Daggerheart Tracker - A beautiful, responsive character tracker for Daggerheart RPG.
Features:
- Modern Material Design-inspired UI
- Smooth animations and transitions
- Responsive layout
- Character management
- Advanced dice rolling system
"""

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.animation import Animation
from utils.settings import SettingsManager

from screens.menu import MenuScreen
from screens.settings import SettingsScreen
from screens.rolls import RollsScreen
from screens.characteristics import CharacteristicsScreen
from screens.ability_checks import AbilityChecksScreen
from screens.combat import CombatScreen
from screens.ability_checks import AbilityChecksScreen
from screens.combat import CombatScreen

# Set responsive window size
Window.size = (1024, 768)
Window.minimum_width = 800
Window.minimum_height = 600

class MainApp(App):
    def build(self):
        self.settings_manager = SettingsManager('settings.json')
        
        # Enhanced character data with more RPG stats
        self.character = {
            'name': 'Mi Personaje',
            'class': 'Guerrero',
            'level': 1,
            'experience': 0,
            'hp_max': 30,
            'hp_current': 30,
            'armor': 2,
            'hope': 0,
            'abilities': {
                'Fuerza': 2,
                'Destreza': 1,
                'Carisma': 0,
                'Constitución': 1,
                'Sabiduría': 0,
                'Inteligencia': -1
            },
            'thresholds': {
                'minor': 10,
                'major': 16,
                'severe': 22
            }
        }
        
        # Create screen manager with smooth transitions
        self.sm = ScreenManager(transition=SlideTransition())
        
        # Add screens
        self.sm.add_widget(MenuScreen(name='menu', app=self))
        self.sm.add_widget(SettingsScreen(name='settings', app=self))
        self.sm.add_widget(RollsScreen(name='rolls', app=self))
        self.sm.add_widget(CharacteristicsScreen(name='characteristics', app=self))
        self.sm.add_widget(AbilityChecksScreen(name='ability_checks', app=self))
        self.sm.add_widget(CombatScreen(name='combat', app=self))
        
        # Set default screen to menu
        self.sm.current = 'menu'
        
        return self.sm

    def switch_screen(self, screen_name, direction='left'):
        """Switch to a screen with optional transition direction"""
        self.sm.transition.direction = direction
        self.sm.current = screen_name

if __name__ == '__main__':
    MainApp().run()
