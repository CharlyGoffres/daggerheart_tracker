# screens/characteristics.py
"""
CharacteristicsScreen: Character sheet showing abilities, HP, and other stats.
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle

class CharacteristicsScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        Window.clearcolor = get_color_from_hex('#eaf6fb')
        
        # Main container
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # Title
        title = Label(
            text='[b]Ficha de Personaje[/b]', 
            markup=True, 
            font_size=36, 
            color=get_color_from_hex('#1b4965'),
            size_hint_y=None,
            height=60
        )
        main_layout.add_widget(title)
        
        # Character abilities section
        abilities_card = self.create_card()
        abilities_layout = BoxLayout(orientation='vertical', spacing=10)
        
        abilities_title = Label(
            text='[b]Habilidades[/b]', 
            markup=True, 
            font_size=24, 
            color=get_color_from_hex('#1b4965'),
            size_hint_y=None,
            height=40
        )
        abilities_layout.add_widget(abilities_title)
        
        # Abilities grid
        abilities_grid = GridLayout(cols=2, spacing=10, size_hint_y=None)
        abilities_grid.bind(minimum_height=abilities_grid.setter('height'))
        
        for ability, modifier in self.app.character.items():
            ability_row = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
            
            ability_label = Label(
                text=f'{ability}:', 
                font_size=20, 
                color=get_color_from_hex('#1b4965'),
                size_hint_x=0.7
            )
            
            modifier_label = Label(
                text=f'{modifier:+d}' if modifier != 0 else '0',
                font_size=20,
                color=get_color_from_hex('#1b4965'),
                size_hint_x=0.3
            )
            
            ability_row.add_widget(ability_label)
            ability_row.add_widget(modifier_label)
            abilities_grid.add_widget(ability_row)
        
        abilities_layout.add_widget(abilities_grid)
        abilities_card.add_widget(abilities_layout)
        main_layout.add_widget(abilities_card)
        
        # Character stats section (HP, Armor, etc.)
        stats_card = self.create_card()
        stats_layout = BoxLayout(orientation='vertical', spacing=10)
        
        stats_title = Label(
            text='[b]Estadísticas[/b]', 
            markup=True, 
            font_size=24, 
            color=get_color_from_hex('#1b4965'),
            size_hint_y=None,
            height=40
        )
        stats_layout.add_widget(stats_title)
        
        # Basic stats
        hp_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        hp_layout.add_widget(Label(text='Puntos de Vida:', font_size=18, color=get_color_from_hex('#1b4965')))
        self.hp_input = TextInput(
            text='30',
            font_size=18,
            multiline=False,
            size_hint_x=0.3,
            background_color=get_color_from_hex('#ffffff'),
            foreground_color=get_color_from_hex('#1b4965')
        )
        hp_layout.add_widget(self.hp_input)
        stats_layout.add_widget(hp_layout)
        
        armor_layout = BoxLayout(orientation='horizontal', spacing=10, size_hint_y=None, height=40)
        armor_layout.add_widget(Label(text='Armadura:', font_size=18, color=get_color_from_hex('#1b4965')))
        self.armor_input = TextInput(
            text='12',
            font_size=18,
            multiline=False,
            size_hint_x=0.3,
            background_color=get_color_from_hex('#ffffff'),
            foreground_color=get_color_from_hex('#1b4965')
        )
        armor_layout.add_widget(self.armor_input)
        stats_layout.add_widget(armor_layout)
        
        stats_card.add_widget(stats_layout)
        main_layout.add_widget(stats_card)
        
        # Buttons
        button_layout = BoxLayout(orientation='horizontal', spacing=20, size_hint_y=None, height=60)
        
        save_btn = Button(
            text='💾 Guardar',
            font_size=24,
            background_color=self.rgba('#97c1a9'),
            color=self.rgba('#ffffff'),
            on_release=self.save_character
        )
        
        back_btn = Button(
            text='⏪ Volver',
            font_size=24,
            background_color=self.rgba('#f4978e'),
            color=self.rgba('#ffffff'),
            on_release=lambda x: self.app.switch_screen('menu')
        )
        
        button_layout.add_widget(save_btn)
        button_layout.add_widget(back_btn)
        main_layout.add_widget(button_layout)
        
        self.add_widget(main_layout)
    
    def create_card(self):
        """Create a card-style container with rounded background"""
        card = BoxLayout(orientation='vertical', padding=20, spacing=10, size_hint_y=None)
        card.bind(minimum_height=card.setter('height'))
        
        with card.canvas.before:
            Color(rgba=get_color_from_hex('#ffffffcc'))
            self.bg_rect = RoundedRectangle(radius=[15], pos=card.pos, size=card.size)
        
        def update_bg_rect(*args):
            self.bg_rect.pos = card.pos
            self.bg_rect.size = card.size
        
        card.bind(pos=update_bg_rect, size=update_bg_rect)
        return card
    
    @staticmethod
    def rgba(hexstr):
        """Convert hex color to RGBA"""
        c = get_color_from_hex(hexstr)
        return c if len(c) == 4 else c + [1.0] * (4 - len(c))
    
    def save_character(self, instance):
        """Save character data"""
        try:
            # Here you could save to a file or database
            # For now, just show a confirmation
            from kivy.uix.popup import Popup
            popup_content = BoxLayout(orientation='vertical', spacing=10, padding=20)
            popup_content.add_widget(Label(
                text='¡Personaje guardado!', 
                font_size=24, 
                color=self.rgba('#1b4965')
            ))
            close_btn = Button(
                text="Cerrar", 
                size_hint=(1, 0.5), 
                font_size=22, 
                background_color=self.rgba('#62b6cb'), 
                color=self.rgba('#ffffff')
            )
            popup_content.add_widget(close_btn)
            popup = Popup(
                title="Guardado", 
                content=popup_content, 
                size_hint=(None, None), 
                size=(300, 200), 
                auto_dismiss=False
            )
            close_btn.bind(on_release=popup.dismiss)
            popup.open()
        except Exception as e:
            print(f"Error saving character: {e}")
