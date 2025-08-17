#!/usr/bin/env python3
"""
Test script to verify button spacing and overlapping fixes
"""

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

from components.platform_config import PlatformConfig
from components.bottom_menu_fixed import FixedBottomMenu

# Set window size for testing
Window.minimum_width = 900
Window.minimum_height = 650
Window.size = (1024, 768)

class ButtonSpacingTestApp(App):
    def build(self):
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Title
        title = Label(
            text='Button Spacing Test - Check for overlapping buttons',
            font_size=24,
            size_hint_y=None,
            height=60,
            color=get_color_from_hex('#ecf0f1')
        )
        main_layout.add_widget(title)
        
        # Platform info
        system_info = PlatformConfig.get_system_info()
        info_text = f"Platform: {system_info['platform']}, Window Size: {Window.size}"
        info_label = Label(
            text=info_text,
            font_size=16,
            size_hint_y=None,
            height=40,
            color=get_color_from_hex('#bdc3c7')
        )
        main_layout.add_widget(info_label)
        
        # Instructions
        instructions = Label(
            text='''Check the bottom menu:
1. Buttons should not overlap each other
2. Text should be clearly visible and centered
3. All 5 buttons should fit within the window width
4. Spacing between buttons should be even
5. Click each button to test functionality''',
            font_size=14,
            color=get_color_from_hex('#95a5a6'),
            halign='left',
            valign='top',
            text_size=(None, None)
        )
        instructions.bind(size=instructions.setter('text_size'))
        main_layout.add_widget(instructions)
        
        # Status label for feedback
        self.status_label = Label(
            text='Status: Ready - Click buttons to test',
            font_size=18,
            size_hint_y=None,
            height=50,
            color=get_color_from_hex('#f39c12')
        )
        main_layout.add_widget(self.status_label)
        
        # Add fixed bottom menu to test
        self.bottom_menu = FixedBottomMenu(self)
        main_layout.add_widget(self.bottom_menu)
        
        # Set dark background
        main_layout.canvas.before.clear()
        with main_layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(rgba=get_color_from_hex('#2c3e50'))
            Rectangle(pos=main_layout.pos, size=main_layout.size)
        
        return main_layout
    
    def switch_screen(self, screen_name):
        """Mock switch screen for testing"""
        self.status_label.text = f"Status: Clicked {screen_name} button - SUCCESS!"
        print(f"Button test: {screen_name} - WORKING")
        
        # Change color briefly to show it worked
        original_color = self.status_label.color
        self.status_label.color = get_color_from_hex('#27ae60')
        from kivy.clock import Clock
        Clock.schedule_once(lambda dt: setattr(self.status_label, 'color', original_color), 1.0)

if __name__ == '__main__':
    print("Starting button spacing test...")
    print("Window size:", Window.size)
    print("Minimum size:", Window.minimum_width, "x", Window.minimum_height)
    ButtonSpacingTestApp().run()
