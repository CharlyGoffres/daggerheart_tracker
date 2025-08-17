#!/usr/bin/env python3
"""
Test script to check button behavior at minimum window size
"""

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.utils import get_color_from_hex
from kivy.core.window import Window
from kivy.clock import Clock

from components.bottom_menu_fixed import FixedBottomMenu

# Test at minimum supported size
Window.minimum_width = 900
Window.minimum_height = 650
Window.size = (900, 650)  # Test at minimum size

class MinimumSizeTestApp(App):
    def build(self):
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title
        title = Label(
            text='Minimum Size Test (900x650)',
            font_size=20,
            size_hint_y=None,
            height=50,
            color=get_color_from_hex('#ecf0f1')
        )
        main_layout.add_widget(title)
        
        # Window info
        self.info_label = Label(
            text=f'Current Size: {Window.size}',
            font_size=14,
            size_hint_y=None,
            height=30,
            color=get_color_from_hex('#bdc3c7')
        )
        main_layout.add_widget(self.info_label)
        
        # Button dimensions info
        self.button_info = Label(
            text='Checking button layout...',
            font_size=12,
            color=get_color_from_hex('#95a5a6'),
            halign='left',
            valign='top'
        )
        main_layout.add_widget(self.button_info)
        
        # Add bottom menu
        self.bottom_menu = FixedBottomMenu(self)
        main_layout.add_widget(self.bottom_menu)
        
        # Schedule button analysis
        Clock.schedule_once(self.analyze_buttons, 1.0)
        
        # Set dark background
        with main_layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(rgba=get_color_from_hex('#2c3e50'))
            Rectangle(pos=main_layout.pos, size=main_layout.size)
        
        return main_layout
    
    def analyze_buttons(self, dt):
        """Analyze button layout for potential overlapping"""
        if hasattr(self.bottom_menu, 'buttons'):
            analysis = []
            buttons = list(self.bottom_menu.buttons.values())
            
            analysis.append(f"Menu Size: {self.bottom_menu.size}")
            analysis.append(f"Menu Padding: {self.bottom_menu.padding}")
            analysis.append(f"Menu Spacing: {self.bottom_menu.spacing}")
            analysis.append(f"Button Count: {len(buttons)}")
            
            if buttons:
                total_button_width = 0
                for i, btn in enumerate(buttons):
                    analysis.append(f"Button {i+1}: {btn.size} at {btn.pos}")
                    total_button_width += btn.width
                
                available_width = self.bottom_menu.width - self.bottom_menu.padding[0] - self.bottom_menu.padding[2]
                spacing_needed = self.bottom_menu.spacing * (len(buttons) - 1)
                total_needed = total_button_width + spacing_needed
                
                analysis.append(f"Available Width: {available_width}")
                analysis.append(f"Total Button Width: {total_button_width}")
                analysis.append(f"Spacing Needed: {spacing_needed}")
                analysis.append(f"Total Needed: {total_needed}")
                
                if total_needed > available_width:
                    analysis.append("⚠️ POTENTIAL OVERLAP DETECTED!")
                else:
                    analysis.append("✅ Buttons fit properly")
            
            self.button_info.text = '\n'.join(analysis)
            self.button_info.text_size = (self.button_info.width, None)
    
    def switch_screen(self, screen_name):
        """Mock switch screen for testing"""
        print(f"Button test: {screen_name} - Working at minimum size")

if __name__ == '__main__':
    MinimumSizeTestApp().run()
