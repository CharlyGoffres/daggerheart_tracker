# components/layout_utils.py
"""
Layout utilities for consistent spacing, centering, and responsive design across all screens
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from components.responsive_utils import ResponsiveUtils

class LayoutUtils:
    """Utility class for consistent layout patterns"""
    
    @staticmethod
    def get_bottom_menu_height():
        """Get the height of the bottom menu based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type == 'mobile':
            return 70
        elif screen_type == 'tablet':
            return 80
        else:
            return 90
    
    @staticmethod
    def get_content_padding():
        """Get responsive padding for content areas"""
        screen_type = ResponsiveUtils.get_screen_type()
        bottom_menu_height = LayoutUtils.get_bottom_menu_height()
        
        if screen_type == 'mobile':
            return [20, 30, 20, bottom_menu_height + 20]  # left, top, right, bottom
        elif screen_type == 'tablet':
            return [30, 40, 30, bottom_menu_height + 30]
        else:
            return [40, 50, 40, bottom_menu_height + 40]
    
    @staticmethod
    def get_content_spacing():
        """Get responsive spacing for content elements"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type == 'mobile':
            return 15
        elif screen_type == 'tablet':
            return 20
        else:
            return 25
    
    @staticmethod
    def create_main_container(app, content_widget, bottom_menu_class):
        """Create a standardized main container with content and bottom menu"""
        main_container = BoxLayout(orientation='vertical')
        
        # Add content
        main_container.add_widget(content_widget)
        
        # Add bottom menu
        bottom_menu = bottom_menu_class(app)
        main_container.add_widget(bottom_menu)
        
        return main_container, bottom_menu
    
    @staticmethod
    def create_scrollable_content():
        """Create a standardized scrollable content area"""
        scroll = ScrollView()
        content_layout = BoxLayout(
            orientation='vertical', 
            size_hint_y=None,
            padding=LayoutUtils.get_content_padding(),
            spacing=LayoutUtils.get_content_spacing()
        )
        content_layout.bind(minimum_height=content_layout.setter('height'))
        
        scroll.add_widget(content_layout)
        return scroll, content_layout
    
    @staticmethod
    def create_centered_header(title_text, font_size=36):
        """Create a centered header with consistent styling"""
        from kivy.uix.label import Label
        from kivy.utils import get_color_from_hex
        
        header = AnchorLayout(size_hint_y=None, height=80)
        title = Label(
            text=title_text,
            markup=True,
            font_size=ResponsiveUtils.get_responsive_font_size(font_size),
            color=get_color_from_hex('#ecf0f1'),
            halign='center',
            valign='middle'
        )
        header.add_widget(title)
        return header, title
    
    @staticmethod
    def update_responsive_layout(content_layout, title_label=None):
        """Update layout properties for responsive design"""
        # Update padding and spacing
        content_layout.padding = LayoutUtils.get_content_padding()
        content_layout.spacing = LayoutUtils.get_content_spacing()
        
        # Update title font size if provided
        if title_label:
            title_label.font_size = ResponsiveUtils.get_responsive_font_size(36)
    
    @staticmethod
    def bind_responsive_updates(content_layout, title_label=None):
        """Bind window resize events for responsive updates"""
        def on_resize(*args):
            LayoutUtils.update_responsive_layout(content_layout, title_label)
        
        Window.bind(on_resize=on_resize)
        return on_resize
    
    @staticmethod
    def create_gradient_background(screen, top_color='#667eea', bottom_color='#764ba2'):
        """Create a beautiful gradient background for screens"""
        with screen.canvas.before:
            # Top gradient color
            Color(rgba=get_color_from_hex(top_color))
            screen.bg_gradient_top = RoundedRectangle(pos=screen.pos, size=(screen.size[0], screen.size[1] * 0.6))
            
            # Bottom gradient color 
            Color(rgba=get_color_from_hex(bottom_color))
            screen.bg_gradient_bottom = RoundedRectangle(pos=(screen.pos[0], screen.pos[1] + screen.size[1] * 0.4), 
                                                       size=(screen.size[0], screen.size[1] * 0.6))
        
        def update_gradient_bg(*args):
            screen.bg_gradient_top.pos = screen.pos
            screen.bg_gradient_top.size = (screen.size[0], screen.size[1] * 0.6)
            screen.bg_gradient_bottom.pos = (screen.pos[0], screen.pos[1] + screen.size[1] * 0.4)
            screen.bg_gradient_bottom.size = (screen.size[0], screen.size[1] * 0.6)
        
        screen.bind(pos=update_gradient_bg, size=update_gradient_bg)
        return update_gradient_bg
