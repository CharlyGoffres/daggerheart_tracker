# components/responsive_utils.py
"""
Responsive utility functions for adapting UI to different screen sizes
Includes Raspberry Pi optimizations
"""

from kivy.core.window import Window
from kivy.metrics import dp, sp
from kivy.clock import Clock
from components.platform_config import PlatformConfig

class ResponsiveUtils:
    """Utility class for responsive design calculations"""
    
    # Breakpoints for different screen sizes
    MOBILE_BREAKPOINT = 600
    TABLET_BREAKPOINT = 900
    DESKTOP_BREAKPOINT = 1200
    
    # Raspberry Pi common screen sizes
    RPI_BREAKPOINTS = {
        'rpi_7inch': (800, 480),    # Official 7" touchscreen
        'rpi_3_5inch': (480, 320),  # Small touchscreen
        'rpi_5inch': (800, 480),    # 5" HDMI display
    }
    
    @staticmethod
    def get_screen_size():
        """Get current window size"""
        return Window.width, Window.height
    
    @staticmethod
    def get_screen_type():
        """Determine screen type based on width, with Raspberry Pi detection"""
        width = Window.width
        system_info = PlatformConfig.get_system_info()
        
        # Special handling for Raspberry Pi
        if system_info.get('is_raspberry_pi', False):
            if width <= 480:
                return 'rpi_small'
            elif width <= 800:
                return 'rpi_medium' 
            else:
                return 'rpi_large'
        
        # Standard breakpoints
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
        if screen_type in ['mobile', 'rpi_small']:
            return [dp(10), dp(15), dp(10), dp(100)]
        elif screen_type in ['tablet', 'rpi_medium']:
            return [dp(20), dp(25), dp(20), dp(110)]
        elif screen_type == 'rpi_large':
            return [dp(25), dp(30), dp(25), dp(120)]
        else:
            return [dp(30), dp(40), dp(30), dp(140)]
    
    @staticmethod
    def get_responsive_spacing():
        """Get responsive spacing based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type in ['mobile', 'rpi_small']:
            return dp(10)
        elif screen_type in ['tablet', 'rpi_medium']:
            return dp(15)
        elif screen_type == 'rpi_large':
            return dp(18)
        else:
            return dp(25)
    
    @staticmethod
    def get_responsive_font_size(base_size):
        """Get responsive font size based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type in ['mobile', 'rpi_small']:
            return sp(base_size * 0.7)
        elif screen_type in ['tablet', 'rpi_medium']:
            return sp(base_size * 0.8)
        elif screen_type == 'rpi_large':
            return sp(base_size * 0.85)
        else:
            return sp(base_size)
    
    @staticmethod
    def get_responsive_button_height():
        """Get responsive button height based on screen size"""
        screen_type = ResponsiveUtils.get_screen_type()
        if screen_type in ['mobile', 'rpi_small']:
            return dp(50)
        elif screen_type in ['tablet', 'rpi_medium']:
            return dp(60)
        elif screen_type == 'rpi_large':
            return dp(65)
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
        if screen_type in ['mobile', 'rpi_small']:
            return dp(80)
        elif screen_type in ['tablet', 'rpi_medium']:
            return dp(85)
        elif screen_type == 'rpi_large':
            return dp(90)
        else:
            return dp(100)
    
    @staticmethod
    def get_touch_target_size():
        """Get minimum touch target size for different platforms"""
        screen_type = ResponsiveUtils.get_screen_type()
        system_info = PlatformConfig.get_system_info()
        
        if system_info.get('is_raspberry_pi', False):
            # Raspberry Pi touchscreens need larger touch targets
            return dp(60)
        elif screen_type in ['mobile', 'rpi_small']:
            return dp(44)  # iOS/Android standard
        else:
            return dp(40)
    
    @staticmethod
    def is_raspberry_pi_optimized():
        """Check if running on Raspberry Pi and should use optimizations"""
        system_info = PlatformConfig.get_system_info()
        return system_info.get('is_raspberry_pi', False)
