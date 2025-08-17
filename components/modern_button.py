# components/modern_button.py
"""
Modern button component with consistent styling across all screens
"""

from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle
from kivy.animation import Animation
from kivy.core.window import Window
from kivy.clock import Clock
from components.responsive_utils import ResponsiveUtils

class ModernButton(Button):
    def __init__(self, bg_color='#34495e', hover_color='#2c3e50', base_font_size=18, **kwargs):
        super().__init__(**kwargs)
        self.bg_color_hex = bg_color
        self.hover_color_hex = hover_color
        self.base_font_size = base_font_size
        self.bg_color = get_color_from_hex(bg_color)
        self.hover_color = get_color_from_hex(hover_color)
        self.normal_color = self.bg_color[:]
        self.background_color = (0, 0, 0, 0)  # Transparent
        
        with self.canvas.before:
            Color(rgba=self.bg_color)
            self.bg_rect = RoundedRectangle(radius=[10], pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.bind(on_press=self.on_button_press)
        self.bind(on_release=self.on_button_release)
        self.color = get_color_from_hex('#ecf0f1')
        
        # Bind to window resize for responsive updates
        Window.bind(on_resize=self.on_window_resize)
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def update_responsive_properties(self, *args):
        """Update button properties based on screen size"""
        # Update font size responsively
        self.font_size = ResponsiveUtils.get_responsive_font_size(self.base_font_size)
        
        # Update button height if not explicitly set
        if not hasattr(self, '_custom_height') and self.size_hint_y is None:
            self.height = ResponsiveUtils.get_responsive_button_height()
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
    def on_button_press(self, *args):
        # Smooth color transition on press
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.hover_color)
            self.bg_rect = RoundedRectangle(radius=[10], pos=self.pos, size=self.size)
    
    def on_button_release(self, *args):
        # Return to normal color
        self.canvas.before.clear()
        with self.canvas.before:
            Color(rgba=self.normal_color)
            self.bg_rect = RoundedRectangle(radius=[10], pos=self.pos, size=self.size)

class ModernActionButton(ModernButton):
    """Action button with special styling for primary actions"""
    def __init__(self, **kwargs):
        # Remove bg_color and hover_color from kwargs if they exist
        kwargs.pop('bg_color', None)
        kwargs.pop('hover_color', None)
        super().__init__(bg_color='#3498db', hover_color='#2980b9', **kwargs)

class ModernDangerButton(ModernButton):
    """Danger button with red styling for destructive actions"""
    def __init__(self, **kwargs):
        # Remove bg_color and hover_color from kwargs if they exist
        kwargs.pop('bg_color', None)
        kwargs.pop('hover_color', None)
        super().__init__(bg_color='#e74c3c', hover_color='#c0392b', **kwargs)

class ModernSuccessButton(ModernButton):
    """Success button with green styling for positive actions"""
    def __init__(self, **kwargs):
        # Remove bg_color and hover_color from kwargs if they exist
        kwargs.pop('bg_color', None)
        kwargs.pop('hover_color', None)
        super().__init__(bg_color='#27ae60', hover_color='#229954', **kwargs)

class ModernWarningButton(ModernButton):
    """Warning button with orange styling for caution actions"""
    def __init__(self, **kwargs):
        # Remove bg_color and hover_color from kwargs if they exist
        kwargs.pop('bg_color', None)
        kwargs.pop('hover_color', None)
        super().__init__(bg_color='#f39c12', hover_color='#e67e22', **kwargs)
