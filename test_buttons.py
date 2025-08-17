#!/usr/bin/env python3
"""
Test script to verify button display and functionality
"""

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.core.window import Window
from components.bottom_menu import BottomMenu, BottomMenuButton

# Set window size
Window.size = (800, 600)

class TestApp(App):
    def __init__(self):
        super().__init__()
        self.current_screen = 'menu'
        
    def build(self):
        layout = BoxLayout(orientation='vertical')
        
        # Status label
        self.status_label = Label(
            text='Current Screen: menu',
            font_size=24,
            size_hint_y=0.8
        )
        layout.add_widget(self.status_label)
        
        # Bottom menu
        self.bottom_menu = BottomMenu(self)
        layout.add_widget(self.bottom_menu)
        
        return layout
    
    def switch_screen(self, screen_name, direction='left'):
        """Test screen switching"""
        self.current_screen = screen_name
        self.status_label.text = f'Current Screen: {screen_name}'
        
        # Update active button
        self.bottom_menu.set_active_button(screen_name)
        print(f"Switched to: {screen_name}")

if __name__ == '__main__':
    TestApp().run()
