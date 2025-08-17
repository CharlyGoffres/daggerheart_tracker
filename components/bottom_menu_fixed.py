# Fixed bottom menu implementation for PC compatibility
# components/bottom_menu_fixed.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from kivy.core.window import Window
from components.platform_config import PlatformConfig
from components.responsive_utils import ResponsiveUtils

class FixedBottomMenuButton(Button):
    def __init__(self, icon, text, screen_name, app, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = screen_name
        self.app = app
        self.icon = icon
        self.button_text = text
        
        # Button styling with responsive defaults
        self.background_color = (0, 0, 0, 0)  # Transparent
        self.size_hint_y = None
        self.markup = True
        self.color = get_color_from_hex('#ecf0f1')
        self.halign = 'center'
        self.valign = 'middle'
        self.text_size = (None, None)
        
        # Initialize background rectangle
        self.bg_rect = None
        
        # Bind events with proper error handling
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.bind(on_press=self.on_button_press)
        self.bind(on_release=self.on_button_release)
        Window.bind(on_resize=self.on_window_resize)
        
        # Schedule responsive update
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def update_responsive_properties(self, *args):
        """Update button properties based on screen size"""
        try:
            screen_type = ResponsiveUtils.get_screen_type()
            
            # Responsive button height
            if screen_type == 'mobile':
                self.height = 60
                icon_size = 12
                text_size = 8
            elif screen_type == 'tablet':
                self.height = 65
                icon_size = 13
                text_size = 9
            else:
                self.height = 70
                icon_size = 14
                text_size = 10
            
            # Update text with responsive sizes
            self.text = f'[b][size={icon_size}]{self.icon}[/size][/b]\n[size={text_size}]{self.button_text}[/size]'
            
            # Update background
            self.update_bg()
        except Exception as e:
            print(f"Error updating responsive properties: {e}")
    
    def update_bg(self, *args):
        """Update background rectangle and text size"""
        try:
            # Clear and recreate the background
            self.canvas.before.clear()
            with self.canvas.before:
                Color(rgba=get_color_from_hex('#34495e'))
                self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
            
            # Update text size for proper text centering
            self.text_size = self.size
        except Exception as e:
            print(f"Error updating button background: {e}")
    
    def on_button_press(self, *args):
        """Handle button press - visual feedback"""
        try:
            # Change color to show press
            self.canvas.before.clear()
            with self.canvas.before:
                Color(rgba=get_color_from_hex('#2980b9'))  # Darker blue for press
                self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
            print(f"Button pressed: {self.screen_name}")
        except Exception as e:
            print(f"Error in button press: {e}")
    
    def on_button_release(self, *args):
        """Handle button release - actual navigation"""
        try:
            print(f"Button released: {self.screen_name}")
            # Switch screen
            self.app.switch_screen(self.screen_name)
            print(f"Successfully switched to: {self.screen_name}")
        except Exception as e:
            print(f"Error switching screen: {e}")
        finally:
            # Reset button color
            Clock.schedule_once(lambda dt: self.update_bg(), 0.1)
    
    def set_active(self, active=True):
        """Set button as active/inactive"""
        try:
            self.canvas.before.clear()
            with self.canvas.before:
                if active:
                    Color(rgba=get_color_from_hex('#3498db'))
                else:
                    Color(rgba=get_color_from_hex('#34495e'))
                self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        except Exception as e:
            print(f"Error setting button active state: {e}")

class FixedBottomMenu(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 100  # Reduced height to minimize overlap
        self.spacing = 6   # Reduced spacing to fit better
        self.padding = [12, 12, 12, 12]  # Reduced padding
        
        # Initialize background rectangle
        self.bg_rect = None
        
        # Bind events
        self.bind(pos=self.update_bg, size=self.update_bg)
        Window.bind(on_resize=self.on_window_resize)
        
        # Menu buttons with fixed configuration
        self.buttons = {}
        
        # Fixed button configuration for PC
        button_configs = [
            ('MENU', 'Menú', 'simple_menu'),
            ('DICE', 'Dados', 'rolls'),
            ('CHAR', 'Personaje', 'characteristics'),
            ('FIGHT', 'Combate', 'combat'),
            ('GEAR', 'Ajustes', 'settings')
        ]
        
        for icon_text, label, screen_name in button_configs:
            btn = FixedBottomMenuButton(
                icon=icon_text,
                text=label,
                screen_name=screen_name,
                app=self.app,
                size_hint_x=0.19  # Optimized for 5 buttons with spacing
            )
            self.buttons[screen_name] = btn
            self.add_widget(btn)
        
        # Schedule responsive update
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def update_responsive_properties(self, *args):
        """Update menu properties based on screen size"""
        try:
            # Responsive height and spacing
            self.height = ResponsiveUtils.get_bottom_menu_height()
            
            screen_type = ResponsiveUtils.get_screen_type()
            if screen_type == 'mobile':
                self.spacing = 4
                self.padding = [8, 8, 8, 8]
            elif screen_type == 'tablet':
                self.spacing = 5
                self.padding = [10, 10, 10, 10]
            else:
                self.spacing = 6
                self.padding = [12, 12, 12, 12]
            
            # Update background
            self.update_bg()
        except Exception as e:
            print(f"Error updating menu responsive properties: {e}")
    
    def update_bg(self, *args):
        """Update background rectangle"""
        try:
            self.canvas.before.clear()
            with self.canvas.before:
                Color(rgba=get_color_from_hex('#2c3e50'))
                self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 0, 0])
        except Exception as e:
            print(f"Error updating menu background: {e}")
    
    def set_active_button(self, screen_name):
        """Update which button appears active"""
        try:
            for name, button in self.buttons.items():
                button.set_active(name == screen_name)
            print(f"Set active button: {screen_name}")
        except Exception as e:
            print(f"Error setting active button: {e}")
