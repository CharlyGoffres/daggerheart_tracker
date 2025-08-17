#!/usr/bin/env python3
"""
Debug script to test button functionality
"""

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex

from components.platform_config import PlatformConfig
from components.bottom_menu_adaptive import AdaptiveBottomMenu

class TestApp(App):
    def build(self):
        # Test layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Title
        title = Label(
            text='Button Test - Click buttons to test functionality',
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
        
        # Platform info
        system_info = PlatformConfig.get_system_info()
        info_text = f"Platform: {system_info['platform']}, Use emoji: {PlatformConfig.use_emoji_buttons()}"
        info_label = Label(
            text=info_text,
            font_size=14,
            size_hint_y=None,
            height=30
        )
        main_layout.add_widget(info_label)
        
        # Test buttons
        test_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=60)
        
        # Simple test button
        simple_btn = Button(
            text='Simple Test',
            background_color=get_color_from_hex('#3498db'),
            on_release=self.simple_button_test
        )
        test_layout.add_widget(simple_btn)
        
        # Data test button
        data_btn = Button(
            text='Data Test',
            background_color=get_color_from_hex('#27ae60'),
            on_release=self.data_button_test
        )
        test_layout.add_widget(data_btn)
        
        main_layout.add_widget(test_layout)
        
        # Add adaptive menu to test navigation
        self.bottom_menu = AdaptiveBottomMenu(self)
        main_layout.add_widget(self.bottom_menu)
        
        return main_layout
    
    def simple_button_test(self, instance):
        """Test simple button functionality"""
        self.status_label.text = "Status: Simple button clicked!"
        print("Simple button test - WORKING")
    
    def data_button_test(self, instance):
        """Test data manipulation"""
        self.status_label.text = "Status: Data button clicked!"
        print("Data button test - WORKING")
    
    def switch_screen(self, screen_name):
        """Mock switch screen for testing"""
        self.status_label.text = f"Status: Would switch to {screen_name}"
        print(f"Navigation test: {screen_name} - WORKING")

if __name__ == '__main__':
    TestApp().run()
