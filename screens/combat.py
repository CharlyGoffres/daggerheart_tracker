# screens/combat.py
"""
CombatScreen: Screen for combat-related actions, weapon/spell rolls, and health/hope management
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from components.bottom_menu_fixed import FixedBottomMenu
from components.modern_button import ModernButton, ModernActionButton, ModernDangerButton, ModernSuccessButton, ModernWarningButton
from components.layout_utils import LayoutUtils
import random

class CombatScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        # Create beautiful gradient background like the menu
        LayoutUtils.create_gradient_background(self, '#ff6b6b', '#ffa726')
        
        # Create main container with standardized layout
        scroll, content_area = LayoutUtils.create_scrollable_content()
        main_container, self.bottom_menu = LayoutUtils.create_main_container(
            self.app, scroll, FixedBottomMenu
        )
        
        self.add_widget(main_container)
        
        # Create centered header
        header, title = LayoutUtils.create_centered_header('[b]⚡ COMBATE[/b]')
        content_area.add_widget(header)
        
        # Health and Hope status
        status_card = self.create_card('#8e44ad')
        status_layout = GridLayout(cols=2, spacing=20, padding=20, size_hint_y=None, height=120)
        
        # Health section
        health_section = BoxLayout(orientation='vertical', spacing=10)
        health_label = Label(
            text='[b]Vida[/b]',
            markup=True,
            font_size=20,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=30
        )
        health_section.add_widget(health_label)
        
        health_display = BoxLayout(orientation='horizontal', spacing=10)
        self.hp_current_label = Label(
            text=str(self.app.character['hp_current']),
            font_size=28,
            color=get_color_from_hex('#e74c3c'),
            size_hint_x=0.25
        )
        
        hp_separator = Label(
            text='/',
            font_size=24,
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.1
        )
        
        hp_max_label = Label(
            text=str(self.app.character['hp_max']),
            font_size=24,
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.25
        )
        
        # HP modification buttons with better spacing
        hp_buttons = BoxLayout(orientation='horizontal', spacing=10, size_hint_x=0.4)
        
        heal_btn = ModernSuccessButton(
            text='+',
            font_size=20,
            size_hint_x=0.5,
            on_release=lambda x: self.modify_hp(1)
        )
        
        damage_btn = ModernDangerButton(
            text='-',
            font_size=20,
            size_hint_x=0.5,
            on_release=lambda x: self.modify_hp(-1)
        )
        
        hp_buttons.add_widget(heal_btn)
        hp_buttons.add_widget(damage_btn)
        
        health_display.add_widget(self.hp_current_label)
        health_display.add_widget(hp_separator)
        health_display.add_widget(hp_max_label)
        health_display.add_widget(hp_buttons)
        health_section.add_widget(health_display)
        
        # Hope section
        hope_section = BoxLayout(orientation='vertical', spacing=10)
        hope_label = Label(
            text='[b]Esperanza[/b]',
            markup=True,
            font_size=20,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=30
        )
        hope_section.add_widget(hope_label)
        
        hope_display = BoxLayout(orientation='horizontal', spacing=10)
        self.hope_label = Label(
            text=str(self.app.character.get('hope', 0)),
            font_size=28,
            color=get_color_from_hex('#f1c40f'),
            size_hint_x=0.6
        )
        
        # Hope modification buttons with better spacing
        hope_buttons = BoxLayout(orientation='horizontal', spacing=10, size_hint_x=0.4)
        
        hope_add_btn = ModernWarningButton(
            text='+',
            font_size=20,
            size_hint_x=0.5,
            on_release=lambda x: self.modify_hope(1)
        )
        
        hope_sub_btn = ModernDangerButton(
            text='-',
            font_size=20,
            size_hint_x=0.5,
            on_release=lambda x: self.modify_hope(-1)
        )
        
        hope_buttons.add_widget(hope_add_btn)
        hope_buttons.add_widget(hope_sub_btn)
        
        hope_display.add_widget(self.hope_label)
        hope_display.add_widget(hope_buttons)
        hope_section.add_widget(hope_display)
        
        status_layout.add_widget(health_section)
        status_layout.add_widget(hope_section)
        status_card.add_widget(status_layout)
        content_area.add_widget(status_card)
        
        # Weapon attack section
        weapon_card = self.create_card('#2c3e50')
        weapon_layout = BoxLayout(orientation='vertical', spacing=15, padding=20, size_hint_y=None, height=200)
        
        weapon_title = Label(
            text='[b]Ataque con Arma[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        weapon_layout.add_widget(weapon_title)
        
        # Weapon selection
        weapon_select_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        weapon_select_layout.add_widget(Label(
            text='Arma:', 
            font_size=18, 
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.3
        ))
        
        self.weapon_spinner = Spinner(
            text='Espada (d8)',
            values=['Espada (d8)', 'Arco (d6)', 'Hacha (d10)', 'Daga (d4)', 'Martillo (d12)'],
            size_hint_x=0.7,
            background_color=self.rgba('#e74c3c'),
            color=self.rgba('#ffffff'),
            font_size=18
        )
        weapon_select_layout.add_widget(self.weapon_spinner)
        weapon_layout.add_widget(weapon_select_layout)
        
        # Weapon modifier
        weapon_mod_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        weapon_mod_layout.add_widget(Label(
            text='Modificador:', 
            font_size=18, 
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.3
        ))
        
        self.weapon_modifier = Spinner(
            text='0',
            values=[str(i) for i in range(-5, 6)],
            size_hint_x=0.7,
            background_color=self.rgba('#e74c3c'),
            color=self.rgba('#ffffff'),
            font_size=18
        )
        weapon_mod_layout.add_widget(self.weapon_modifier)
        weapon_layout.add_widget(weapon_mod_layout)
        
        # Weapon roll button
        weapon_roll_btn = ModernDangerButton(
            text='🗡️ ATACAR',
            font_size=20,
            size_hint_y=None,
            height=50,
            on_release=self.roll_weapon_attack
        )
        weapon_layout.add_widget(weapon_roll_btn)
        
        weapon_card.add_widget(weapon_layout)
        content_area.add_widget(weapon_card)
        
        # Spell attack section
        spell_card = self.create_card('#9b59b6')
        spell_layout = BoxLayout(orientation='vertical', spacing=15, padding=20, size_hint_y=None, height=200)
        
        spell_title = Label(
            text='[b]Lanzar Hechizo[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        spell_layout.add_widget(spell_title)
        
        # Spell selection
        spell_select_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        spell_select_layout.add_widget(Label(
            text='Hechizo:', 
            font_size=18, 
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.3
        ))
        
        self.spell_spinner = Spinner(
            text='Bola de Fuego (d10)',
            values=['Bola de Fuego (d10)', 'Rayo de Hielo (d8)', 'Curación (d6)', 'Misil Mágico (d4)', 'Tormenta (d12)'],
            size_hint_x=0.7,
            background_color=self.rgba('#9b59b6'),
            color=self.rgba('#ffffff'),
            font_size=18
        )
        spell_select_layout.add_widget(self.spell_spinner)
        spell_layout.add_widget(spell_select_layout)
        
        # Spell modifier
        spell_mod_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        spell_mod_layout.add_widget(Label(
            text='Modificador:', 
            font_size=18, 
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.3
        ))
        
        self.spell_modifier = Spinner(
            text='0',
            values=[str(i) for i in range(-5, 6)],
            size_hint_x=0.7,
            background_color=self.rgba('#9b59b6'),
            color=self.rgba('#ffffff'),
            font_size=18
        )
        spell_mod_layout.add_widget(self.spell_modifier)
        spell_layout.add_widget(spell_mod_layout)
        
        # Spell roll button
        spell_roll_btn = ModernActionButton(
            text='🔮 LANZAR',
            font_size=20,
            size_hint_y=None,
            height=50,
            bg_color='#9b59b6',
            hover_color='#8e44ad',
            on_release=self.roll_spell_attack
        )
        spell_layout.add_widget(spell_roll_btn)
        
        spell_card.add_widget(spell_layout)
        content_area.add_widget(spell_card)
        
        # Results display
        self.results_card = self.create_card('#34495e')
        self.results_layout = BoxLayout(orientation='vertical', spacing=15, padding=20, size_hint_y=None, height=200)
        
        results_title = Label(
            text='[b]Último Resultado[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        self.results_layout.add_widget(results_title)
        
        self.results_label = Label(
            text='No se han hecho tiradas aún',
            font_size=16,
            color=get_color_from_hex('#bdc3c7'),
            text_size=(None, None),
            halign='center'
        )
        self.results_layout.add_widget(self.results_label)
        
        self.results_card.add_widget(self.results_layout)
        content_area.add_widget(self.results_card)
        
        # Bind responsive updates
        LayoutUtils.bind_responsive_updates(content_area, title)
    
    def on_enter(self):
        """Called when entering the screen"""
        super().on_enter()
        self.bottom_menu.set_active_button('combat')
        self.update_status_display()
    
    @staticmethod
    def rgba(hexstr):
        c = get_color_from_hex(hexstr)
        return c if len(c) == 4 else c + [1.0] * (4 - len(c))
    
    def create_card(self, bg_color):
        """Create a card widget with rounded background"""
        anchor = AnchorLayout(anchor_x='center', anchor_y='center', size_hint_y=None)
        
        with anchor.canvas.before:
            Color(rgba=get_color_from_hex(bg_color))
            anchor.bg_rect = RoundedRectangle(pos=anchor.pos, size=anchor.size, radius=[15])
        
        anchor.bind(pos=lambda instance, value: setattr(anchor.bg_rect, 'pos', value))
        anchor.bind(size=lambda instance, value: setattr(anchor.bg_rect, 'size', value))
        
        return anchor
    
    def modify_hp(self, amount):
        """Modify current HP"""
        current = self.app.character['hp_current']
        max_hp = self.app.character['hp_max']
        new_hp = max(0, min(max_hp, current + amount))
        self.app.character['hp_current'] = new_hp
        self.update_status_display()
    
    def modify_hope(self, amount):
        """Modify hope"""
        current = self.app.character.get('hope', 0)
        new_hope = max(0, current + amount)
        self.app.character['hope'] = new_hope
        self.update_status_display()
    
    def update_status_display(self):
        """Update HP and Hope displays"""
        self.hp_current_label.text = str(self.app.character['hp_current'])
        self.hope_label.text = str(self.app.character.get('hope', 0))
    
    def roll_weapon_attack(self, *args):
        """Roll weapon attack"""
        weapon_text = self.weapon_spinner.text
        modifier = int(self.weapon_modifier.text)
        
        # Extract die type from weapon text
        die_type = int(weapon_text.split('d')[1].split(')')[0])
        weapon_name = weapon_text.split(' (')[0]
        
        # Roll the die
        roll = random.randint(1, die_type)
        total = roll + modifier
        
        result_text = f"""[b]Ataque con Arma[/b]
[b]Arma:[/b] {weapon_name}
[b]Dado:[/b] d{die_type}
[b]Resultado:[/b] {roll}
[b]Modificador:[/b] {modifier:+d}
[b]Daño Total:[/b] [color=#e74c3c][b]{total}[/b][/color]"""
        
        self.results_label.text = result_text
        self.results_label.markup = True
    
    def roll_spell_attack(self, *args):
        """Roll spell attack"""
        spell_text = self.spell_spinner.text
        modifier = int(self.spell_modifier.text)
        
        # Extract die type from spell text
        die_type = int(spell_text.split('d')[1].split(')')[0])
        spell_name = spell_text.split(' (')[0]
        
        # Roll the die
        roll = random.randint(1, die_type)
        total = roll + modifier
        
        result_text = f"""[b]Lanzar Hechizo[/b]
[b]Hechizo:[/b] {spell_name}
[b]Dado:[/b] d{die_type}
[b]Resultado:[/b] {roll}
[b]Modificador:[/b] {modifier:+d}
[b]Daño Total:[/b] [color=#9b59b6][b]{total}[/b][/color]"""
        
        self.results_label.text = result_text
        self.results_label.markup = True
