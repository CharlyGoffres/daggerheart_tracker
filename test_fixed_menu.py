#!/usr/bin/env python3
"""
Test the fixed bottom menu implementation
"""

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

from components.bottom_menu_fixed import FixedBottomMenu

class FixedMenuTestApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Title
        title = Label(
            text='Fixed Menu Test - Click navigation buttons to test',
            font_size=20,
            size_hint_y=None,
            height=50
        )
        main_layout.add_widget(title)
        
        # Status label
        self.status_label = Label(
            text='Status: Ready',
            font_size=16,
            size_hint_y=None,
            height=50
        )
        main_layout.add_widget(self.status_label)
        
        # Current screen indicator
        self.current_screen_label = Label(
            text='Current Screen: menu',
            font_size=14,
            size_hint_y=None,
            height=30
        )
        main_layout.add_widget(self.current_screen_label)
        
        # Add some content area
        content_area = Label(
            text='This is the content area.\nClick the navigation buttons below to test screen switching.',
            font_size=16,
            halign='center',
            valign='middle'
        )
        main_layout.add_widget(content_area)
        
        # Add fixed bottom menu
        self.bottom_menu = FixedBottomMenu(self)
        main_layout.add_widget(self.bottom_menu)
        
        return main_layout
    
    def switch_screen(self, screen_name):
        """Mock switch screen for testing"""
        self.status_label.text = f"Status: Switched to {screen_name}"
        self.current_screen_label.text = f"Current Screen: {screen_name}"
        self.bottom_menu.set_active_button(screen_name)
        print(f"Navigation test: {screen_name} - SUCCESS")

if __name__ == '__main__':
    FixedMenuTestApp().run()
