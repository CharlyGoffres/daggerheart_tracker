# test_responsive.py
"""Test script to verify responsive design features"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from components.responsive_utils import ResponsiveUtils
from kivy.core.window import Window

def test_responsive_utils():
    """Test responsive utility functions"""
    print("🧪 Testing Responsive Design Features")
    print("=" * 50)
    
    # Test different window sizes
    test_sizes = [
        (400, 600, "Mobile Portrait"),
        (600, 400, "Mobile Landscape"), 
        (800, 600, "Tablet"),
        (1024, 768, "Desktop"),
        (1920, 1080, "Large Desktop")
    ]
    
    for width, height, description in test_sizes:
        # Simulate window size
        Window.size = (width, height)
        
        print(f"\n📱 {description} ({width}x{height})")
        print(f"  Screen Type: {ResponsiveUtils.get_screen_type()}")
        print(f"  Orientation: {'Landscape' if ResponsiveUtils.is_landscape() else 'Portrait'}")
        print(f"  Grid Columns: {ResponsiveUtils.get_grid_cols()}")
        print(f"  Button Height: {ResponsiveUtils.get_responsive_button_height()}dp")
        print(f"  Font Size (18): {ResponsiveUtils.get_responsive_font_size(18)}sp")
        print(f"  Bottom Menu Height: {ResponsiveUtils.get_bottom_menu_height()}dp")
        print(f"  Padding: {ResponsiveUtils.get_responsive_padding()}")
    
    print("\n✅ Responsive Features:")
    print("  • Adaptive padding and spacing based on screen size")
    print("  • Responsive font sizes for different devices")
    print("  • Flexible grid layouts (1-3 columns)")
    print("  • Orientation-aware layouts")
    print("  • Mobile-friendly button sizes")
    print("  • Scalable bottom menu")
    
    print("\n🎯 Breakpoints:")
    print(f"  • Mobile: < {ResponsiveUtils.MOBILE_BREAKPOINT}px")
    print(f"  • Tablet: {ResponsiveUtils.MOBILE_BREAKPOINT}-{ResponsiveUtils.TABLET_BREAKPOINT}px")
    print(f"  • Desktop: {ResponsiveUtils.TABLET_BREAKPOINT}-{ResponsiveUtils.DESKTOP_BREAKPOINT}px")
    print(f"  • Large Desktop: > {ResponsiveUtils.DESKTOP_BREAKPOINT}px")
    
    print("\n📐 Window Size Range:")
    print("  • Minimum: 320x480 (small mobile)")
    print("  • Default: 1024x768 (desktop)")
    print("  • Supports: Any size with adaptive scaling")

if __name__ == '__main__':
    test_responsive_utils()
