# Adaptive bottom menu that works well on all platforms
# components/bottom_menu_adaptive.py

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.clock import Clock
from components.platform_config import PlatformConfig

class AdaptiveBottomMenuButton(Button):
    def __init__(self, icon, text, screen_name, app, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = screen_name
        self.app = app
        self.icon = icon
        self.button_text = text
        
        # Button styling
        self.background_color = (0, 0, 0, 0)  # Transparent
        self.size_hint_y = None
        self.height = 80
        self.markup = True
        
        # Set button content based on platform
        if PlatformConfig.use_emoji_buttons():
            # Use emoji layout for platforms with good emoji support
            self._setup_emoji_layout()
        else:
            # Use text-based layout for better PC compatibility
            self._setup_text_layout()
        
        # Initialize background rectangle
        self.bg_rect = None
        
        # Bind events
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.bind(on_press=self.on_button_press)
        
        # Schedule background initialization
        Clock.schedule_once(self.update_bg, 0.1)
    
    def _setup_emoji_layout(self):
        """Setup layout with emoji icons"""
        layout = BoxLayout(orientation='vertical', spacing=2, padding=[5, 10, 5, 10])
        
        icon_label = Label(
            text=self.icon,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=0.6,
            markup=True,
            halign='center',
            valign='middle'
        )
        icon_label.bind(size=icon_label.setter('text_size'))
        
        text_label = Label(
            text=self.button_text,
            font_size=12,
            color=get_color_from_hex('#bdc3c7'),
            size_hint_y=0.4,
            markup=True,
            halign='center',
            valign='middle'
        )
        text_label.bind(size=text_label.setter('text_size'))
        
        layout.add_widget(icon_label)
        layout.add_widget(text_label)
        self.add_widget(layout)
    
    def _setup_text_layout(self):
        """Setup layout with text-based icons for better PC compatibility"""
        self.text = f'[b][size=16]{self.icon}[/size][/b]\n[size=11]{self.button_text}[/size]'
        self.color = get_color_from_hex('#ecf0f1')
        self.halign = 'center'
        self.valign = 'middle'
        # Set initial text_size
        self.text_size = (None, None)
        self.bind(size=self._update_text_size)
    
    def _update_text_size(self, *args):
        """Update text size when button size changes"""
        self.text_size = self.size
    
    def update_bg(self, *args):
        """Update background rectangle"""
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#34495e'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
    
    def on_button_press(self, *args):
        """Handle button press"""
        print(f"Button pressed: {self.screen_name}")  # Debug output
        try:
            self.app.switch_screen(self.screen_name)
            print(f"Successfully switched to: {self.screen_name}")
        except Exception as e:
            print(f"Error switching screen: {e}")
    
    def set_active(self, active=True):
        """Set button as active/inactive"""
        self.canvas.before.clear()
        with self.canvas.before:
            if active:
                Color(rgba=get_color_from_hex('#3498db'))
            else:
                Color(rgba=get_color_from_hex('#34495e'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

class AdaptiveBottomMenu(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 120
        self.spacing = 12  # Increased spacing to prevent overlapping
        self.padding = [20, 15, 20, 15]  # Increased horizontal padding
        
        # Initialize background rectangle
        self.bg_rect = None
        
        # Bind events
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Menu buttons
        self.buttons = {}
        
        # Get platform-specific button configuration
        button_configs = PlatformConfig.get_button_config()
        
        # Create buttons
        for screen_name, config in button_configs.items():
            btn = AdaptiveBottomMenuButton(
                icon=config['icon'],
                text=config['text'],
                screen_name=screen_name,
                app=self.app,
                size_hint_x=0.19  # Optimized for 5 buttons
            )
            self.buttons[screen_name] = btn
            self.add_widget(btn)
        
        # Schedule background initialization
        Clock.schedule_once(self.update_bg, 0.1)
    
    def update_bg(self, *args):
        """Update background rectangle"""
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#2c3e50'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 0, 0])
    
    def set_active_button(self, screen_name):
        """Update which button appears active"""
        for name, button in self.buttons.items():
            button.set_active(name == screen_name)
