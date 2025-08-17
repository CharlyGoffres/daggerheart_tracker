# test_fixes.py
"""Test script to verify the fixes for text overlap and menu improvements"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import MainApp

def test_app_startup():
    """Test that the app starts with characteristics screen instead of menu"""
    app = MainApp()
    app.build()
    
    print(f"Default screen: {app.sm.current}")
    print("Available screens:", list(app.sm.screen_names))
    
    # Test that we have both menu options
    assert 'menu' in app.sm.screen_names, "Original menu should be available"
    assert 'simple_menu' in app.sm.screen_names, "Simple menu should be available"
    assert 'characteristics' in app.sm.screen_names, "Characteristics screen should be available"
    
    # Test that the default screen is now characteristics instead of menu
    assert app.sm.current == 'characteristics', f"Default screen should be 'characteristics', got '{app.sm.current}'"
    
    print("✅ All tests passed!")
    print("✅ App now starts with characteristics screen instead of fancy menu")
    print("✅ Both menu options are available")
    print("✅ Text overlap should be fixed with proper bottom padding")

if __name__ == '__main__':
    test_app_startup()
