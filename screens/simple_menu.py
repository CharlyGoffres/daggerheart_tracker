# screens/simple_menu.py
"""
SimpleMenuScreen: A cleaner, simpler menu alternative to the fancy main menu
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle
from kivy.clock import Clock
from components.bottom_menu_fixed import FixedBottomMenu
from components.responsive_utils import ResponsiveUtils
from components.responsive_layout import ResponsiveBoxLayout, ResponsiveGridLayout
from components.layout_utils import LayoutUtils

class SimpleMenuButton(Button):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.background_color = (0, 0, 0, 0)  # Transparent
        
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#34495e'))
            self.bg_rect = RoundedRectangle(radius=[10], pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.color = get_color_from_hex('#ecf0f1')
        
        # Bind to window resize for responsive updates
        Window.bind(on_resize=self.on_window_resize)
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def update_responsive_properties(self, *args):
        """Update button properties based on screen size"""
        self.font_size = ResponsiveUtils.get_responsive_font_size(18)
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size

class SimpleMenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        # Create simple background
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#2c3e50'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Create main content with standardized layout
        main_layout = BoxLayout(
            orientation='vertical',
            padding=LayoutUtils.get_content_padding(),
            spacing=LayoutUtils.get_content_spacing()
        )
        
        # Simple title with responsive font
        title_container = LayoutUtils.create_centered_header('DAGGERHEART TRACKER', 32)[0]
        main_layout.add_widget(title_container)
        
        # Responsive navigation grid with proper centering
        nav_container = BoxLayout(orientation='vertical', size_hint_y=0.7)
        nav_grid = ResponsiveGridLayout(auto_cols=True, size_hint=(0.8, None), pos_hint={'center_x': 0.5})
        # Calculate height based on number of buttons and screen type
        nav_grid.height = ResponsiveUtils.get_responsive_button_height() * 3 + ResponsiveUtils.get_responsive_spacing() * 2
        
        # Navigation buttons
        buttons = [
            ('Dados', 'rolls'),
            ('Personaje', 'characteristics'),
            ('Chequeos', 'ability_checks'),
            ('Combate', 'combat'),
            ('Configuración', 'settings'),
            ('Salir', 'exit')
        ]
        
        for text, action in buttons:
            if action == 'exit':
                btn = SimpleMenuButton(
                    text=text,
                    on_release=lambda x: self.app.stop()
                )
            else:
                btn = SimpleMenuButton(
                    text=text,
                    on_release=lambda x, screen=action: self.app.switch_screen(screen)
                )
            nav_grid.add_widget(btn)
        
        nav_container.add_widget(nav_grid)
        main_layout.add_widget(nav_container)
        
        # Create main container with standardized layout
        main_container, self.bottom_menu = LayoutUtils.create_main_container(
            self.app, main_layout, FixedBottomMenu
        )
        
        self.add_widget(main_container)
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        # This will trigger responsive updates in all responsive components
        pass
    
    def on_enter(self):
        """Called when entering the screen"""
        super().on_enter()
        if hasattr(self, 'bottom_menu'):
            # Don't highlight any button on the main menu
            for button in self.bottom_menu.buttons.values():
                button.set_active(False)
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
