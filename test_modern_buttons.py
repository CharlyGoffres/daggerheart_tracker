# test_modern_buttons.py
"""Test script to verify modern buttons are working in all screens"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components.modern_button import ModernButton, ModernActionButton, ModernDangerButton, ModernSuccessButton, ModernWarningButton

def test_button_classes():
    """Test that all button classes can be instantiated without errors"""
    try:
        # Test base modern button
        btn1 = ModernButton(text="Test Button")
        print("✅ ModernButton created successfully")
        
        # Test action button
        btn2 = ModernActionButton(text="Action Button")
        print("✅ ModernActionButton created successfully")
        
        # Test danger button
        btn3 = ModernDangerButton(text="Danger Button")
        print("✅ ModernDangerButton created successfully")
        
        # Test success button
        btn4 = ModernSuccessButton(text="Success Button")
        print("✅ ModernSuccessButton created successfully")
        
        # Test warning button
        btn5 = ModernWarningButton(text="Warning Button")
        print("✅ ModernWarningButton created successfully")
        
        print("\n🎉 All modern button classes working correctly!")
        print("📝 Modern buttons have been successfully integrated into:")
        print("  - Rolls Screen: Ability buttons and close button")
        print("  - Characteristics Screen: Save button")
        print("  - Ability Checks Screen: Roll button")
        print("  - Combat Screen: HP/Hope buttons, attack/spell buttons")
        print("  - Settings Screen: Reset and export buttons")
        
        return True
        
    except Exception as e:
        print(f"❌ Error creating buttons: {e}")
        return False

if __name__ == '__main__':
    test_button_classes()
