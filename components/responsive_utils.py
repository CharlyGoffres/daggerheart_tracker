# components/responsive_utils.py
"""
Responsive utility functions for adapting UI to different screen sizes
"""

from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.clock import Clock

class ResponsiveUtils:
    """Utility class for responsive design calculations"""
    
    # Breakpoints for different screen sizes
    MOBILE_BREAKPOINT = 600
    TABLET_BREAKPOINT = 900
    DESKTOP_BREAKPOINT = 1200
    
    @staticmethod
    def get_screen_size():
        """Get current window size"""
        return Window.width, Window.height
    
    @staticmethod
    def get_screen_type():
        """Determine screen type based on width"""
        width = Window.width
        if width < ResponsiveUtils.MOBILE_BREAKPOINT:
            return 'mobile'
        elif width < ResponsiveUtils.TABLET_BREAKPOINT:
            return 'tablet'
        elif width < ResponsiveUtils.DESKTOP_BREAKPOINT:
            return 'desktop'
        else:
            return 'large_desktop'
    
    @staticmethod
    def is_landscape():
        """Check if screen is in landscape orientation"""
        return Window.width > Window.height
    
    @staticmethod
    def is_portrait():
        """Check if screen is in portrait orientation"""
        return Window.height > Window.width
    
    @staticmethod
    def get_responsive_padding():
        """Get responsive padding based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type == 'mobile':
            return [dp(15), dp(20), dp(15), dp(120)]
        elif screen_type == 'tablet':
            return [dp(25), dp(30), dp(25), dp(130)]
        else:
            return [dp(30), dp(40), dp(30), dp(140)]
    
    @staticmethod
    def get_responsive_spacing():
        """Get responsive spacing based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type == 'mobile':
            return dp(15)
        elif screen_type == 'tablet':
            return dp(20)
        else:
            return dp(25)
    
    @staticmethod
    def get_responsive_font_size(base_size):
        """Get responsive font size based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type == 'mobile':
            return sp(base_size * 0.8)
        elif screen_type == 'tablet':
            return sp(base_size * 0.9)
        else:
            return sp(base_size)
    
    @staticmethod
    def get_responsive_button_height():
        """Get responsive button height based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type == 'mobile':
            return dp(60)
        elif screen_type == 'tablet':
            return dp(70)
        else:
            return dp(80)
    
    @staticmethod
    def get_responsive_card_padding():
        """Get responsive card padding based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type == 'mobile':
            return dp(15)
        elif screen_type == 'tablet':
            return dp(18)
        else:
            return dp(20)
    
    @staticmethod
    def get_grid_cols():
        """Get responsive grid columns based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        width = Window.width
        
        if screen_type == 'mobile':
            return 1 if ResponsiveUtils.is_portrait() else 2
        elif screen_type == 'tablet':
            return 2 if ResponsiveUtils.is_portrait() else 3
        else:
            return 2 if ResponsiveUtils.is_portrait() else 3
    
    @staticmethod
    def get_bottom_menu_height():
        """Get responsive bottom menu height"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type == 'mobile':
            return dp(90)
        elif screen_type == 'tablet':
            return dp(95)
        else:
            return dp(100)
