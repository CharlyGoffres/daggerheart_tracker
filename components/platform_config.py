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
            'is_linux': platform.system() == 'Linux'
        }
    
    @staticmethod
    def use_emoji_buttons():
        """Determine if emoji buttons should be used"""
        system_info = PlatformConfig.get_system_info()
        
        # On Windows, emoji support can be inconsistent
        # Use text-based buttons for better compatibility
        if system_info['is_windows']:
            return False
        
        # Mac generally has good emoji support
        if system_info['is_mac']:
            return True
            
        # Linux emoji support varies
        if system_info['is_linux']:
            return False
            
        return False
    
    @staticmethod
    def get_button_config():
        """Get optimal button configuration for current platform"""
        if PlatformConfig.use_emoji_buttons():
            return {
                'rolls': {'icon': '🎲', 'text': 'Dados'},
                'ability_checks': {'icon': '🎯', 'text': 'Chequeos'},
                'characteristics': {'icon': '⚔️', 'text': 'Personaje'},
                'combat': {'icon': '⚡', 'text': 'Combate'},
                'settings': {'icon': '⚙️', 'text': 'Ajustes'}
            }
        else:
            return {
                'rolls': {'icon': 'DICE', 'text': 'Dados'},
                'ability_checks': {'icon': 'CHECK', 'text': 'Chequeos'},
                'characteristics': {'icon': 'CHAR', 'text': 'Personaje'},
                'combat': {'icon': 'FIGHT', 'text': 'Combate'},
                'settings': {'icon': 'GEAR', 'text': 'Ajustes'}
            }
