# main.py
"""
Daggerheart Tracker - A beautiful, responsive character tracker for Daggerheart RPG.
Features:
- Modern Material Design-inspired UI
- Smooth animations and transitions
- Responsive layout with Raspberry Pi optimizations
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
from components.platform_config import PlatformConfig

from screens.menu import MenuScreen
from screens.simple_menu import SimpleMenuScreen
from screens.settings import SettingsScreen
from screens.rolls import RollsScreen
from screens.characteristics import CharacteristicsScreen
from screens.ability_checks import AbilityChecksScreen
from screens.combat import CombatScreen
from screens.ability_checks import AbilityChecksScreen
from screens.combat import CombatScreen

# Set responsive window size with platform detection
system_info = PlatformConfig.get_system_info()
if system_info.get('is_raspberry_pi', False):
    # Raspberry Pi optimizations
    rpi_opts = PlatformConfig.get_raspberry_pi_optimizations()
    Window.size = rpi_opts['window_size']
    Window.minimum_width = 480
    Window.minimum_height = 320
else:
    # Standard desktop/mobile sizes
    Window.minimum_width = 320  # Allow smaller mobile screens
    Window.minimum_height = 480  # Allow smaller mobile screens
    Window.size = (1024, 768)   # Default desktop size

class MainApp(App):
    def build(self):
        self.settings_manager = SettingsManager('settings.json')
        
        # Check if running on Raspberry Pi for optimizations
        system_info = PlatformConfig.get_system_info()
        self.is_raspberry_pi = system_info.get('is_raspberry_pi', False)
        
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
        
        # Create screen manager with optimized transitions for Raspberry Pi
        if self.is_raspberry_pi:
            rpi_opts = PlatformConfig.get_raspberry_pi_optimizations()
            transition = SlideTransition(duration=rpi_opts['animation_duration'])
        else:
            transition = SlideTransition()
            
        self.sm = ScreenManager(transition=transition)
        
        # Add screens
        self.sm.add_widget(MenuScreen(name='menu', app=self))
        self.sm.add_widget(SimpleMenuScreen(name='simple_menu', app=self))
        self.sm.add_widget(SettingsScreen(name='settings', app=self))
        self.sm.add_widget(RollsScreen(name='rolls', app=self))
        self.sm.add_widget(CharacteristicsScreen(name='characteristics', app=self))
        self.sm.add_widget(AbilityChecksScreen(name='ability_checks', app=self))
        self.sm.add_widget(CombatScreen(name='combat', app=self))
        
        # Set default screen to characteristics (skip the fancy menu)
        self.sm.current = 'characteristics'
        
        return self.sm

    def switch_screen(self, screen_name, direction='left'):
        """Switch to a screen with optional transition direction"""
        self.sm.transition.direction = direction
        self.sm.current = screen_name

if __name__ == '__main__':
    MainApp().run()
