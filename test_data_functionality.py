#!/usr/bin/env python3
"""
Comprehensive test for data functionality in the rolls screen
"""

import kivy
kivy.require('2.0.0')
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
import random

class DataTestApp(App):
    def build(self):
        self.character = {
            'name': 'Test Character',
            'abilities': {
                'Fuerza': 2,
                'Destreza': 1,
                'Carisma': 0,
                'Constitución': 1,
                'Sabiduría': 0,
                'Inteligencia': -1
            }
        }
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=20)
        
        # Title
        title = Label(
            text='Data Functionality Test',
            font_size=20,
            size_hint_y=None,
            height=50
        )
        main_layout.add_widget(title)
        
        # Character data display
        char_info = Label(
            text=f"Character: {self.character['name']}",
            font_size=16,
            size_hint_y=None,
            height=30
        )
        main_layout.add_widget(char_info)
        
        # Abilities display
        abilities_text = "Abilities: " + ", ".join([f"{k}: {v:+d}" for k, v in self.character['abilities'].items()])
        abilities_label = Label(
            text=abilities_text,
            font_size=14,
            size_hint_y=None,
            height=30
        )
        main_layout.add_widget(abilities_label)
        
        # Result display
        self.result_label = Label(
            text='Click an ability button to test dice rolling',
            font_size=16,
            size_hint_y=None,
            height=60
        )
        main_layout.add_widget(self.result_label)
        
        # Test buttons for abilities
        buttons_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=80)
        
        colors = ['#e74c3c', '#3498db', '#9b59b6', '#e67e22', '#27ae60', '#f39c12']
        for i, (ability, modifier) in enumerate(self.character['abilities'].items()):
            btn = Button(
                text=f'{ability}\n({modifier:+d})',
                background_color=get_color_from_hex(colors[i]),
                font_size=14,
                on_release=lambda x, a=ability, m=modifier: self.test_roll(a, m)
            )
            buttons_layout.add_widget(btn)
        
        main_layout.add_widget(buttons_layout)
        
        # Data manipulation test
        data_test_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=60)
        
        modify_btn = Button(
            text='Modify Character Data',
            background_color=get_color_from_hex('#95a5a6'),
            on_release=self.modify_data
        )
        data_test_layout.add_widget(modify_btn)
        
        reset_btn = Button(
            text='Reset Data',
            background_color=get_color_from_hex('#34495e'),
            on_release=self.reset_data
        )
        data_test_layout.add_widget(reset_btn)
        
        main_layout.add_widget(data_test_layout)
        
        return main_layout
    
    def test_roll(self, ability, modifier):
        """Test dice rolling with character data"""
        # Roll 2d12
        dice1 = random.randint(1, 12)
        dice2 = random.randint(1, 12)
        total = dice1 + dice2 + modifier
        
        result_text = f"Rolled {ability}: {dice1} + {dice2} + {modifier:+d} = {total}"
        self.result_label.text = result_text
        print(f"Data test - {result_text}")
    
    def modify_data(self, instance):
        """Test data modification"""
        # Randomly modify an ability
        ability = random.choice(list(self.character['abilities'].keys()))
        old_value = self.character['abilities'][ability]
        self.character['abilities'][ability] = random.randint(-2, 3)
        new_value = self.character['abilities'][ability]
        
        self.result_label.text = f"Modified {ability}: {old_value:+d} → {new_value:+d}"
        print(f"Data modification test - {ability}: {old_value} → {new_value}")
    
    def reset_data(self, instance):
        """Test data reset"""
        self.character['abilities'] = {
            'Fuerza': 2,
            'Destreza': 1,
            'Carisma': 0,
            'Constitución': 1,
            'Sabiduría': 0,
            'Inteligencia': -1
        }
        self.result_label.text = "Character data reset to defaults"
        print("Data reset test - Character data reset")

if __name__ == '__main__':
    DataTestApp().run()
