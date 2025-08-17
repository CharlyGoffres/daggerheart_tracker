#!/usr/bin/env python3
"""
Script to update all screen files to use the fixed bottom menu
"""

import os
import re

# Files to update
screen_files = [
    'screens/rolls.py',
    'screens/characteristics.py',
    'screens/ability_checks.py',
    'screens/combat.py',
    'screens/settings.py',
    'screens/menu.py'
]

for file_path in screen_files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the import
        old_import = 'from components.bottom_menu_adaptive import AdaptiveBottomMenu'
        new_import = 'from components.bottom_menu_fixed import FixedBottomMenu'
        
        # Replace the menu instantiation
        old_menu = 'self.bottom_menu = AdaptiveBottomMenu(self.app)'
        new_menu = 'self.bottom_menu = FixedBottomMenu(self.app)'
        
        if old_import in content:
            content = content.replace(old_import, new_import)
            print(f"Updated import in {file_path}")
        
        if old_menu in content:
            content = content.replace(old_menu, new_menu)
            print(f"Updated menu instantiation in {file_path}")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    else:
        print(f"File not found: {file_path}")

print("Update complete!")
