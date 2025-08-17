# components/responsive_layout.py
"""
Responsive layout components that adapt to different screen sizes
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.clock import Clock
from components.responsive_utils import ResponsiveUtils

class ResponsiveBoxLayout(BoxLayout):
    """BoxLayout that adapts its properties based on screen size"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.bind(size=self.on_size_change)
        Window.bind(on_resize=self.on_window_resize)
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_size_change(self, *args):
        """Called when the layout size changes"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def update_responsive_properties(self, *args):
        """Update layout properties based on current screen size"""
        # Update padding if not explicitly set
        if not hasattr(self, '_custom_padding'):
            self.padding = ResponsiveUtils.get_responsive_padding()
        
        # Update spacing if not explicitly set
        if not hasattr(self, '_custom_spacing'):
            self.spacing = ResponsiveUtils.get_responsive_spacing()

class ResponsiveGridLayout(GridLayout):
    """GridLayout that adapts its columns based on screen size"""
    
    def __init__(self, auto_cols=True, **kwargs):
        self.auto_cols = auto_cols
        super().__init__(**kwargs)
        self.bind(size=self.on_size_change)
        Window.bind(on_resize=self.on_window_resize)
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_size_change(self, *args):
        """Called when the layout size changes"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def update_responsive_properties(self, *args):
        """Update layout properties based on current screen size"""
        # Update columns if auto_cols is enabled
        if self.auto_cols:
            self.cols = ResponsiveUtils.get_grid_cols()
        
        # Update spacing
        self.spacing = ResponsiveUtils.get_responsive_spacing()

class ResponsiveCard(BoxLayout):
    """Card component that adapts its styling based on screen size"""
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.size_hint_y = None
        self.bind(minimum_height=self.setter('height'))
        Window.bind(on_resize=self.on_window_resize)
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        Clock.schedule_once(self.update_responsive_properties, 0.1)
    
    def update_responsive_properties(self, *args):
        """Update card properties based on current screen size"""
        padding = ResponsiveUtils.get_responsive_card_padding()
        self.padding = [padding, padding, padding, padding]
        self.spacing = ResponsiveUtils.get_responsive_spacing() * 0.6
