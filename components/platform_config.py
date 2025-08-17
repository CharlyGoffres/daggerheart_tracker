# Configuration file for platform-specific settings
# components/platform_config.py

import platform
import os

class PlatformConfig:
    """Platform-specific configuration for optimal display"""
    
    @staticmethod
    def get_system_info():
        """Get system information for optimal configuration"""
        return {
            'platform': platform.system(),
            'machine': platform.machine(),
            'python_version': platform.python_version(),
            'is_windows': platform.system() == 'Windows',
            'is_mac': platform.system() == 'Darwin',
            'is_linux': platform.system() == 'Linux',
            'is_raspberry_pi': PlatformConfig.is_raspberry_pi()
        }
    
    @staticmethod
    def is_raspberry_pi():
        """Detect if running on Raspberry Pi"""
        try:
            # Check for Raspberry Pi hardware
            with open('/proc/cpuinfo', 'r') as f:
                cpuinfo = f.read()
                return 'BCM' in cpuinfo or 'Raspberry Pi' in cpuinfo
        except:
            # Check machine type as fallback
            machine = platform.machine()
            return machine.startswith('arm') or machine.startswith('aarch64')
        return False
    
    @staticmethod
    def use_emoji_buttons():
        """Determine if emoji buttons should be used"""
        system_info = PlatformConfig.get_system_info()
        
        # On Raspberry Pi, use Unicode dice symbols for better compatibility
        if system_info['is_raspberry_pi']:
            return True
        
        # On Windows, emoji support can be inconsistent
        # Use text-based buttons for better compatibility
        if system_info['is_windows']:
            return False
        
        # Mac generally has good emoji support
        if system_info['is_mac']:
            return True
            
        # Linux emoji support varies, but use Unicode symbols
        if system_info['is_linux']:
            return True
            
        return False
    
    @staticmethod
    def get_button_config():
        """Get optimal button configuration for current platform"""
        system_info = PlatformConfig.get_system_info()
        
        if PlatformConfig.use_emoji_buttons():
            if system_info['is_raspberry_pi']:
                # Use Unicode dice and symbols for Raspberry Pi
                return {
                    'rolls': {'icon': '⚀⚁', 'text': 'Dados'},
                    'ability_checks': {'icon': '�', 'text': 'Chequeos'},
                    'characteristics': {'icon': '⚔', 'text': 'Personaje'},
                    'combat': {'icon': '⚡', 'text': 'Combate'},
                    'settings': {'icon': '⚙', 'text': 'Ajustes'},
                    'simple_menu': {'icon': '☰', 'text': 'Menú'}
                }
            else:
                # Standard emoji for other platforms
                return {
                    'rolls': {'icon': '�🎲', 'text': 'Dados'},
                    'ability_checks': {'icon': '🎯', 'text': 'Chequeos'},
                    'characteristics': {'icon': '⚔️', 'text': 'Personaje'},
                    'combat': {'icon': '⚡', 'text': 'Combate'},
                    'settings': {'icon': '⚙️', 'text': 'Ajustes'},
                    'simple_menu': {'icon': '☰', 'text': 'Menú'}
                }
        else:
            return {
                'rolls': {'icon': 'DICE', 'text': 'Dados'},
                'ability_checks': {'icon': 'CHECK', 'text': 'Chequeos'},
                'characteristics': {'icon': 'CHAR', 'text': 'Personaje'},
                'combat': {'icon': 'FIGHT', 'text': 'Combate'},
                'settings': {'icon': 'GEAR', 'text': 'Ajustes'},
                'simple_menu': {'icon': 'MENU', 'text': 'Menú'}
            }
    
    @staticmethod
    def get_raspberry_pi_optimizations():
        """Get Raspberry Pi specific optimizations"""
        return {
            'window_size': (800, 480),  # Common RPi touchscreen size
            'font_scale': 0.9,          # Slightly smaller fonts for small screens
            'touch_target_size': 60,    # Minimum touch target size
            'animation_duration': 0.15, # Faster animations for better performance
            'use_hardware_acceleration': True,
            'enable_touch_mode': True
        }
