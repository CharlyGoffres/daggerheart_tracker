# Alternative button implementation with better PC compatibility
# components/bottom_menu_pc.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle, Rectangle
from kivy.utils import get_color_from_hex
from kivy.clock import Clock

class PCBottomMenuButton(Button):
    def __init__(self, icon_text, text, screen_name, app, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = screen_name
        self.app = app
        self.icon_text = icon_text
        self.button_text = text
        
        # Button styling
        self.background_color = (0, 0, 0, 0)  # Transparent
        self.size_hint_y = None
        self.height = 80
        self.markup = True
        
        # Simple button layout
        self.text = f'[b][size=18]{icon_text}[/size][/b]\n[size=12]{text}[/size]'
        self.color = get_color_from_hex('#ecf0f1')
        self.halign = 'center'
        self.valign = 'middle'
        self.text_size = (None, None)
        
        # Initialize background rectangle
        self.bg_rect = None
        
        # Bind events
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.bind(on_press=self.on_button_press)
        
        # Schedule background initialization
        Clock.schedule_once(self.update_bg, 0.1)
    
    def update_bg(self, *args):
        # Clear and recreate the background
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#34495e'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        
        # Update text size
        self.text_size = self.size
    
    def on_button_press(self, *args):
        # Simple button press
        self.app.switch_screen(self.screen_name)
    
    def set_active(self, active=True):
        """Set button as active/inactive"""
        self.canvas.before.clear()
        with self.canvas.before:
            if active:
                Color(rgba=get_color_from_hex('#3498db'))
            else:
                Color(rgba=get_color_from_hex('#34495e'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

class PCBottomMenu(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 120
        self.spacing = 8
        self.padding = [15, 15, 15, 15]
        
        # Initialize background rectangle
        self.bg_rect = None
        
        # Bind events
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Menu buttons with text-based icons
        self.buttons = {}
        
        # Create buttons with PC-compatible icons
        button_configs = [
            ('DICE', 'Dados', 'rolls'),
            ('CHECK', 'Chequeos', 'ability_checks'),
            ('CHAR', 'Personaje', 'characteristics'),
            ('FIGHT', 'Combate', 'combat'),
            ('GEAR', 'Ajustes', 'settings')
        ]
        
        for icon_text, label, screen_name in button_configs:
            btn = PCBottomMenuButton(
                icon_text=icon_text,
                text=label,
                screen_name=screen_name,
                app=self.app,
                size_hint_x=0.2
            )
            self.buttons[screen_name] = btn
            self.add_widget(btn)
        
        # Schedule background initialization
        Clock.schedule_once(self.update_bg, 0.1)
    
    def update_bg(self, *args):
        # Clear and recreate the background
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#2c3e50'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 0, 0])
    
    def set_active_button(self, screen_name):
        """Update which button appears active"""
        for name, button in self.buttons.items():
            button.set_active(name == screen_name)
