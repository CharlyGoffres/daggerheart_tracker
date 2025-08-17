# screens/characteristics.py
"""
CharacteristicsScreen: Beautiful character sheet with modern design and responsive layout
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle, Line
from components.bottom_menu_adaptive import AdaptiveBottomMenu

class CharacteristicsScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        # Create gradient background
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#1a252f'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Main container with bottom menu
        main_container = BoxLayout(orientation='vertical')
        
        # Main scrollable container
        scroll = ScrollView()
        main_layout = BoxLayout(orientation='vertical', padding=[30, 40, 30, 20], spacing=25, size_hint_y=None)
        main_layout.bind(minimum_height=main_layout.setter('height'))
        
        # Header with title
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, spacing=20)
        
        title = Label(
            text='[b]⚔️ FICHA DE PERSONAJE[/b]',
            markup=True,
            font_size=36,
            color=get_color_from_hex('#ecf0f1'),
            halign='center'
        )
        
        header.add_widget(title)
        main_layout.add_widget(header)
        
        # Character identity card
        identity_card = self.create_card('#2c3e50')
        identity_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        identity_title = Label(
            text='[b]Información del Personaje[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        identity_layout.add_widget(identity_title)
        
        # Character basic info in grid
        info_grid = GridLayout(cols=2, spacing=15, size_hint_y=None, height=120)
        
        # Name input
        info_grid.add_widget(Label(text='Nombre:', font_size=18, color=get_color_from_hex('#bdc3c7')))
        self.name_input = TextInput(
            text=self.app.character['name'],
            font_size=18,
            multiline=False,
            background_color=self.rgba('#34495e'),
            foreground_color=self.rgba('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        info_grid.add_widget(self.name_input)
        
        # Class input
        info_grid.add_widget(Label(text='Clase:', font_size=18, color=get_color_from_hex('#bdc3c7')))
        self.class_input = TextInput(
            text=self.app.character['class'],
            font_size=18,
            multiline=False,
            background_color=self.rgba('#34495e'),
            foreground_color=self.rgba('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        info_grid.add_widget(self.class_input)
        
        # Level input
        info_grid.add_widget(Label(text='Nivel:', font_size=18, color=get_color_from_hex('#bdc3c7')))
        self.level_input = TextInput(
            text=str(self.app.character['level']),
            font_size=18,
            multiline=False,
            background_color=self.rgba('#34495e'),
            foreground_color=self.rgba('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        info_grid.add_widget(self.level_input)
        
        identity_layout.add_widget(info_grid)
        identity_card.add_widget(identity_layout)
        main_layout.add_widget(identity_card)
        
        # Health and resources card
        health_card = self.create_card('#c0392b', 0.1)
        health_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        health_title = Label(
            text='[b]❤️ Salud y Recursos[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        health_layout.add_widget(health_title)
        
        # HP section
        hp_section = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=60)
        
        hp_label = Label(
            text='Puntos de Vida:',
            font_size=20,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_x=0.4
        )
        hp_section.add_widget(hp_label)
        
        # Current HP
        self.hp_current_input = TextInput(
            text=str(self.app.character['hp_current']),
            font_size=24,
            multiline=False,
            background_color=self.rgba('#e74c3c'),
            foreground_color=self.rgba('#ffffff'),
            size_hint_x=0.25,
            halign='center'
        )
        hp_section.add_widget(self.hp_current_input)
        
        hp_section.add_widget(Label(text='/', font_size=24, color=get_color_from_hex('#ecf0f1'), size_hint_x=0.1))
        
        # Max HP
        self.hp_max_input = TextInput(
            text=str(self.app.character['hp_max']),
            font_size=24,
            multiline=False,
            background_color=self.rgba('#27ae60'),
            foreground_color=self.rgba('#ffffff'),
            size_hint_x=0.25,
            halign='center'
        )
        hp_section.add_widget(self.hp_max_input)
        
        health_layout.add_widget(hp_section)
        
        # Armor section
        armor_section = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        armor_section.add_widget(Label(text='🛡️ Armadura:', font_size=18, color=get_color_from_hex('#ecf0f1')))
        
        self.armor_input = TextInput(
            text=str(self.app.character['armor']),
            font_size=18,
            multiline=False,
            background_color=self.rgba('#95a5a6'),
            foreground_color=self.rgba('#2c3e50'),
            size_hint_x=0.3
        )
        armor_section.add_widget(self.armor_input)
        armor_section.add_widget(BoxLayout())  # Spacer
        
        health_layout.add_widget(armor_section)
        health_card.add_widget(health_layout)
        main_layout.add_widget(health_card)
        
        # Abilities card
        abilities_card = self.create_card('#27ae60', 0.1)
        abilities_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        abilities_title = Label(
            text='[b]⚡ Habilidades[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        abilities_layout.add_widget(abilities_title)
        
        # Abilities grid
        abilities_grid = GridLayout(cols=2, spacing=15, size_hint_y=None)
        abilities_grid.bind(minimum_height=abilities_grid.setter('height'))
        
        self.ability_inputs = {}
        ability_colors = {
            'Fuerza': '#e74c3c',
            'Destreza': '#f39c12', 
            'Carisma': '#9b59b6',
            'Constitución': '#27ae60',
            'Sabiduría': '#3498db',
            'Inteligencia': '#95a5a6'
        }
        
        for ability, modifier in self.app.character['abilities'].items():
            ability_card = self.create_ability_card(ability, modifier, ability_colors.get(ability, '#34495e'))
            abilities_grid.add_widget(ability_card)
        
        abilities_layout.add_widget(abilities_grid)
        abilities_card.add_widget(abilities_layout)
        main_layout.add_widget(abilities_card)
        
        # Thresholds card
        thresholds_card = self.create_card('#8e44ad', 0.1)
        thresholds_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        thresholds_title = Label(
            text='[b]🎯 Umbrales de Dificultad[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        thresholds_layout.add_widget(thresholds_title)
        
        # Thresholds grid
        thresholds_grid = GridLayout(cols=3, spacing=15, size_hint_y=None, height=80)
        
        threshold_data = [
            ('Menor', self.app.character['thresholds']['minor'], '#f39c12'),
            ('Mayor', self.app.character['thresholds']['major'], '#e67e22'),
            ('Severo', self.app.character['thresholds']['severe'], '#c0392b')
        ]
        
        for name, value, color in threshold_data:
            threshold_box = BoxLayout(orientation='vertical', spacing=5)
            
            threshold_label = Label(
                text=name,
                font_size=16,
                color=get_color_from_hex('#ecf0f1'),
                size_hint_y=None,
                height=25
            )
            
            threshold_value = Label(
                text=str(value),
                font_size=28,
                color=get_color_from_hex(color),
                size_hint_y=None,
                height=45
            )
            
            threshold_box.add_widget(threshold_label)
            threshold_box.add_widget(threshold_value)
            thresholds_grid.add_widget(threshold_box)
        
        thresholds_layout.add_widget(thresholds_grid)
        thresholds_card.add_widget(thresholds_layout)
        main_layout.add_widget(thresholds_card)
        
        # Save button
        save_btn = Button(
            text='💾 Guardar Cambios',
            font_size=22,
            size_hint=(None, None),
            size=(250, 60),
            background_color=self.rgba('#3498db'),
            color=self.rgba('#ffffff'),
            on_release=self.save_character
        )
        
        save_container = AnchorLayout(size_hint_y=None, height=80)
        save_container.add_widget(save_btn)
        main_layout.add_widget(save_container)
        
        scroll.add_widget(main_layout)
        main_container.add_widget(scroll)
        
        # Add bottom menu
        self.bottom_menu = AdaptiveBottomMenu(self.app)
        main_container.add_widget(self.bottom_menu)
        
        self.add_widget(main_container)
    
    def on_enter(self):
        """Called when entering the screen"""
        super().on_enter()
        self.bottom_menu.set_active_button('characteristics')
    
    def create_card(self, bg_color, alpha=0.9):
        """Create a modern card container"""
        card = BoxLayout(orientation='vertical', size_hint_y=None)
        card.bind(minimum_height=card.setter('height'))
        
        with card.canvas.before:
            Color(rgba=get_color_from_hex(bg_color) + [alpha])
            card.bg_rect = RoundedRectangle(radius=[20], pos=card.pos, size=card.size)
        
        def update_card_bg(*args):
            card.bg_rect.pos = card.pos
            card.bg_rect.size = card.size
            
        card.bind(pos=update_card_bg, size=update_card_bg)
        return card
    
    def create_ability_card(self, ability, modifier, color):
        """Create an individual ability card"""
        card = BoxLayout(orientation='vertical', spacing=5, size_hint_y=None, height=100, padding=10)
        
        with card.canvas.before:
            Color(rgba=get_color_from_hex(color) + [0.2])
            card.bg_rect = RoundedRectangle(radius=[15], pos=card.pos, size=card.size)
            Color(rgba=get_color_from_hex(color))
            card.border_rect = Line(rounded_rectangle=(card.pos[0], card.pos[1], card.size[0], card.size[1], 15), width=2)
        
        def update_ability_graphics(*args):
            card.bg_rect.pos = card.pos
            card.bg_rect.size = card.size
            card.border_rect.rounded_rectangle = (card.pos[0], card.pos[1], card.size[0], card.size[1], 15)
        
        card.bind(pos=update_ability_graphics, size=update_ability_graphics)
        
        # Ability name
        ability_label = Label(
            text=ability,
            font_size=18,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=30,
            halign='center',
            valign='middle',
            text_size=(None, None)
        )
        card.add_widget(ability_label)
        
        # Modifier input
        modifier_input = TextInput(
            text=str(modifier),
            font_size=24,
            multiline=False,
            background_color=self.rgba(color),
            foreground_color=self.rgba('#ffffff'),
            size_hint_y=None,
            height=40,
            halign='center'
        )
        
        self.ability_inputs[ability] = modifier_input
        card.add_widget(modifier_input)
        
        return card
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
    def rgba(self, hexstr):
        c = get_color_from_hex(hexstr)
        return c if len(c) == 4 else c + [1.0] * (4 - len(c))
    
    def save_character(self, instance):
        """Save character changes"""
        try:
            # Update character data
            self.app.character['name'] = self.name_input.text
            self.app.character['class'] = self.class_input.text
            self.app.character['level'] = int(self.level_input.text)
            self.app.character['hp_current'] = int(self.hp_current_input.text)
            self.app.character['hp_max'] = int(self.hp_max_input.text)
            self.app.character['armor'] = int(self.armor_input.text)
            
            # Update abilities
            for ability, input_widget in self.ability_inputs.items():
                self.app.character['abilities'][ability] = int(input_widget.text)
            
            # Visual feedback
            instance.text = '✅ ¡Guardado!'
            instance.background_color = self.rgba('#27ae60')
            
            # Reset button after 2 seconds
            Clock.schedule_once(lambda dt: self.reset_save_button(instance), 2)
            
        except ValueError:
            # Error feedback
            instance.text = '❌ Error'
            instance.background_color = self.rgba('#e74c3c')
            Clock.schedule_once(lambda dt: self.reset_save_button(instance), 2)
    
    def reset_save_button(self, button):
        """Reset save button to original state"""
        button.text = '💾 Guardar Cambios'
        button.background_color = self.rgba('#3498db')

from kivy.clock import Clock
