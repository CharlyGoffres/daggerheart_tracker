# screens/ability_checks.py
"""
AbilityChecksScreen: Screen for rolling 2d12 ability checks with hope/fear mechanics
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.scrollview import ScrollView
from kivy.clock import Clock
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from components.bottom_menu_fixed import FixedBottomMenu
import random

class AbilityChecksScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        # Create gradient background
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#1a252f'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Main layout with bottom menu
        main_container = BoxLayout(orientation='vertical')
        
        # Content area
        content_area = BoxLayout(orientation='vertical', padding=[30, 40, 30, 20], spacing=25)
        
        # Header
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, spacing=20)
        
        title = Label(
            text='[b]🎯 CHEQUEOS DE HABILIDAD[/b]',
            markup=True,
            font_size=36,
            color=get_color_from_hex('#ecf0f1'),
            halign='center'
        )
        
        header.add_widget(title)
        content_area.add_widget(header)
        
        # Ability selection card
        ability_card = self.create_card('#2c3e50')
        ability_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        ability_title = Label(
            text='[b]Seleccionar Habilidad[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        ability_layout.add_widget(ability_title)
        
        # Ability spinner
        ability_selection_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        ability_selection_layout.add_widget(Label(
            text='Habilidad:', 
            font_size=18, 
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.3
        ))
        
        self.ability_spinner = Spinner(
            text='Fuerza',
            values=list(self.app.character['abilities'].keys()),
            size_hint_x=0.7,
            background_color=self.rgba('#3498db'),
            color=self.rgba('#ffffff'),
            font_size=18
        )
        ability_selection_layout.add_widget(self.ability_spinner)
        ability_layout.add_widget(ability_selection_layout)
        
        # Modifier input
        modifier_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        modifier_layout.add_widget(Label(
            text='Modificador:', 
            font_size=18, 
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.3
        ))
        
        self.modifier_spinner = Spinner(
            text='0',
            values=[str(i) for i in range(-5, 6)],
            size_hint_x=0.7,
            background_color=self.rgba('#3498db'),
            color=self.rgba('#ffffff'),
            font_size=18
        )
        modifier_layout.add_widget(self.modifier_spinner)
        ability_layout.add_widget(modifier_layout)
        
        ability_card.add_widget(ability_layout)
        content_area.add_widget(ability_card)
        
        # Hope counter display
        hope_card = self.create_card('#8e44ad')
        hope_layout = BoxLayout(orientation='horizontal', spacing=20, padding=20)
        
        hope_label = Label(
            text='[b]Esperanza:[/b]',
            markup=True,
            font_size=20,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_x=0.4
        )
        
        self.hope_counter = Label(
            text=str(self.app.character.get('hope', 0)),
            font_size=32,
            color=get_color_from_hex('#f1c40f'),
            size_hint_x=0.6
        )
        
        hope_layout.add_widget(hope_label)
        hope_layout.add_widget(self.hope_counter)
        hope_card.add_widget(hope_layout)
        content_area.add_widget(hope_card)
        
        # Roll button
        self.roll_button = Button(
            text='🎲 TIRAR 2D12',
            font_size=24,
            size_hint_y=None,
            height=80,
            background_color=self.rgba('#27ae60'),
            color=self.rgba('#ffffff'),
            on_release=self.roll_ability_check
        )
        content_area.add_widget(self.roll_button)
        
        # Results display
        self.results_card = self.create_card('#34495e')
        self.results_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
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
            font_size=18,
            color=get_color_from_hex('#bdc3c7'),
            text_size=(None, None),
            halign='center'
        )
        self.results_layout.add_widget(self.results_label)
        
        self.results_card.add_widget(self.results_layout)
        content_area.add_widget(self.results_card)
        
        main_container.add_widget(content_area)
        
        # Add bottom menu
        self.bottom_menu = FixedBottomMenu(self.app)
        main_container.add_widget(self.bottom_menu)
        
        self.add_widget(main_container)
    
    def on_enter(self):
        """Called when entering the screen"""
        super().on_enter()
        self.bottom_menu.set_active_button('ability_checks')
        self.update_hope_display()
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
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
    
    def roll_ability_check(self, *args):
        """Roll 2d12 for ability check with hope/fear mechanics"""
        # Get selected ability and modifier
        ability = self.ability_spinner.text
        ability_value = self.app.character['abilities'][ability]
        modifier = int(self.modifier_spinner.text)
        
        # Roll hope and fear dice
        hope_die = random.randint(1, 12)
        fear_die = random.randint(1, 12)
        
        # Determine which die is higher
        if hope_die > fear_die:
            result_die = hope_die
            die_type = "Esperanza"
            die_color = '#f1c40f'
            # Add 1 hope to counter
            current_hope = self.app.character.get('hope', 0)
            self.app.character['hope'] = current_hope + 1
            hope_gained = True
        elif fear_die > hope_die:
            result_die = fear_die
            die_type = "Miedo"
            die_color = '#e74c3c'
            hope_gained = False
        else:  # Tie
            result_die = hope_die  # Could be either since they're equal
            die_type = "Empate"
            die_color = '#95a5a6'
            hope_gained = False
        
        # Calculate final result
        total = result_die + ability_value + modifier
        
        # Determine success level
        thresholds = self.app.character['thresholds']
        if total >= thresholds['severe']:
            success_level = "Éxito Crítico"
            success_color = '#27ae60'
        elif total >= thresholds['major']:
            success_level = "Éxito Mayor"
            success_color = '#2ecc71'
        elif total >= thresholds['minor']:
            success_level = "Éxito Menor"
            success_color = '#f39c12'
        else:
            success_level = "Fallo"
            success_color = '#e74c3c'
        
        # Update results display
        result_text = f"""[b]Habilidad:[/b] {ability} ({ability_value:+d})
[b]Modificador:[/b] {modifier:+d}

[b]Dados:[/b]
[color={die_color}]● Esperanza: {hope_die}[/color]
[color=#e74c3c]● Miedo: {fear_die}[/color]

[b]Dado usado:[/b] [color={die_color}]{die_type} ({result_die})[/color]
[b]Total:[/b] {result_die} + {ability_value} + {modifier} = [b]{total}[/b]

[color={success_color}][b]{success_level}[/b][/color]"""
        
        if hope_gained:
            result_text += f"\n\n[color=#f1c40f]¡+1 Esperanza![/color]"
        
        self.results_label.text = result_text
        self.results_label.markup = True
        
        # Update hope display
        self.update_hope_display()
        
        # Animate button
        self.animate_roll_button()
    
    def update_hope_display(self):
        """Update the hope counter display"""
        self.hope_counter.text = str(self.app.character.get('hope', 0))
    
    def animate_roll_button(self):
        """Animate the roll button"""
        # Change color temporarily
        original_color = self.roll_button.background_color
        Animation(background_color=self.rgba('#e67e22'), duration=0.1).start(self.roll_button)
        Clock.schedule_once(lambda dt: Animation(background_color=original_color, duration=0.1).start(self.roll_button), 0.1)
