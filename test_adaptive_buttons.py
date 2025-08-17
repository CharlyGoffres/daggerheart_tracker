#!/usr/bin/env python3
"""
Test script to verify the adaptive button implementation in the main app
"""

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from components.bottom_menu_adaptive import AdaptiveBottomMenu
from components.platform_config import PlatformConfig

# Set window size
Window.size = (1024, 768)

class MainTestApp(App):
    def __init__(self):
        super().__init__()
        self.current_screen = 'menu'
        
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Status area
        status_layout = BoxLayout(orientation='vertical', size_hint_y=0.8, padding=20, spacing=10)
        
        # System info
        system_info = PlatformConfig.get_system_info()
        system_text = f"Platform: {system_info['platform']}\n"
        system_text += f"Machine: {system_info['machine']}\n"
        system_text += f"Python: {system_info['python_version']}\n"
        system_text += f"Using emoji buttons: {PlatformConfig.use_emoji_buttons()}"
        
        system_label = Label(
            text=system_text,
            font_size=16,
            size_hint_y=0.3,
            halign='left',
            valign='top'
        )
        system_label.bind(size=system_label.setter('text_size'))
        status_layout.add_widget(system_label)
        
        # Current screen status
        self.status_label = Label(
            text='Current Screen: menu\nClick buttons to test navigation',
            font_size=24,
            size_hint_y=0.7,
            halign='center',
            valign='middle'
        )
        self.status_label.bind(size=self.status_label.setter('text_size'))
        status_layout.add_widget(self.status_label)
        
        layout.add_widget(status_layout)
        
        # Bottom menu with adaptive buttons
        self.bottom_menu = AdaptiveBottomMenu(self)
        layout.add_widget(self.bottom_menu)
        
        return layout
    
    def switch_screen(self, screen_name, direction='left'):
        """Test screen switching"""
        self.current_screen = screen_name
        self.status_label.text = f'Current Screen: {screen_name}\nButtons are working correctly!'
        
        # Update active button
        self.bottom_menu.set_active_button(screen_name)
        print(f"Successfully switched to: {screen_name}")

if __name__ == '__main__':
    MainTestApp().run()
