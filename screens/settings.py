# screens/settings.py
"""
SettingsScreen: Modern settings interface with beautiful styling
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle
from kivy.clock import Clock
from components.bottom_menu_fixed import FixedBottomMenu

class SettingsScreen(Screen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        # Create gradient background
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#8e44ad'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Main container with bottom menu
        main_container = BoxLayout(orientation='vertical')
        
        # Content area with scroll
        scroll = ScrollView()
        main_layout = BoxLayout(orientation='vertical', padding=[30, 40, 30, 20], spacing=25, size_hint_y=None)
        main_layout.bind(minimum_height=main_layout.setter('height'))
        
        # Header with title
        header = BoxLayout(orientation='horizontal', size_hint_y=None, height=80, spacing=20)
        
        title = Label(
            text='[b]⚙️ CONFIGURACIÓN[/b]',
            markup=True,
            font_size=36,
            color=get_color_from_hex('#ecf0f1'),
            halign='center'
        )
        
        header.add_widget(title)
        main_layout.add_widget(header)
        
        # Application settings card
        app_card = self.create_card('#9b59b6')
        app_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        app_title = Label(
            text='[b]📱 Configuración de la Aplicación[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        app_layout.add_widget(app_title)
        
        # Theme settings
        theme_section = self.create_setting_row(
            '🎨 Tema Oscuro',
            'Usar colores oscuros para la interfaz',
            'switch',
            self.app.settings_manager.get('dark_theme', True),
            self.toggle_theme
        )
        app_layout.add_widget(theme_section)
        
        # Sound settings
        sound_section = self.create_setting_row(
            '🔊 Sonidos',
            'Reproducir efectos de sonido',
            'switch',
            self.app.settings_manager.get('sounds_enabled', True),
            self.toggle_sounds
        )
        app_layout.add_widget(sound_section)
        
        # Animations settings
        anim_section = self.create_setting_row(
            '✨ Animaciones',
            'Mostrar animaciones y transiciones',
            'switch',
            self.app.settings_manager.get('animations_enabled', True),
            self.toggle_animations
        )
        app_layout.add_widget(anim_section)
        
        app_card.add_widget(app_layout)
        main_layout.add_widget(app_card)
        
        # Game settings card
        game_card = self.create_card('#e67e22')
        game_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        game_title = Label(
            text='[b]🎲 Configuración del Juego[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        game_layout.add_widget(game_title)
        
        # Auto-save settings
        autosave_section = self.create_setting_row(
            '💾 Guardado Automático',
            'Guardar cambios automáticamente',
            'switch',
            self.app.settings_manager.get('auto_save', True),
            self.toggle_autosave
        )
        game_layout.add_widget(autosave_section)
        
        # Dice animation speed
        speed_section = self.create_setting_row(
            '⚡ Velocidad de Dados',
            'Velocidad de animación de los dados',
            'slider',
            self.app.settings_manager.get('dice_speed', 50),
            self.change_dice_speed
        )
        game_layout.add_widget(speed_section)
        
        game_card.add_widget(game_layout)
        main_layout.add_widget(game_card)
        
        # Character settings card
        char_card = self.create_card('#27ae60')
        char_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        char_title = Label(
            text='[b]⚔️ Configuración del Personaje[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        char_layout.add_widget(char_title)
        
        # Quick actions
        actions_grid = GridLayout(cols=2, spacing=15, size_hint_y=None, height=120)
        
        reset_btn = Button(
            text='🔄 Resetear\nPersonaje',
            font_size=18,
            background_color=self.rgba('#e74c3c'),
            color=self.rgba('#ffffff'),
            on_release=self.reset_character
        )
        actions_grid.add_widget(reset_btn)
        
        export_btn = Button(
            text='📤 Exportar\nDatos',
            font_size=18,
            background_color=self.rgba('#3498db'),
            color=self.rgba('#ffffff'),
            on_release=self.export_character
        )
        actions_grid.add_widget(export_btn)
        
        char_layout.add_widget(actions_grid)
        char_card.add_widget(char_layout)
        main_layout.add_widget(char_card)
        
        # Info section
        info_card = self.create_card('#34495e')
        info_layout = BoxLayout(orientation='vertical', spacing=10, padding=20)
        
        info_title = Label(
            text='[b]ℹ️ Información[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        info_layout.add_widget(info_title)
        
        version_label = Label(
            text='Daggerheart Tracker v2.0\nCreado con ❤️ para jugadores de RPG',
            font_size=16,
            color=get_color_from_hex('#bdc3c7'),
            halign='center'
        )
        info_layout.add_widget(version_label)
        
        info_card.add_widget(info_layout)
        main_layout.add_widget(info_card)
        
        scroll.add_widget(main_layout)
        main_container.add_widget(scroll)
        
        # Add bottom menu
        self.bottom_menu = FixedBottomMenu(self.app)
        main_container.add_widget(self.bottom_menu)
        
        self.add_widget(main_container)
    
    def on_enter(self):
        """Called when entering the screen"""
        super().on_enter()
        self.bottom_menu.set_active_button('settings')
    
    def create_card(self, bg_color):
        """Create a modern card container"""
        card = BoxLayout(orientation='vertical', size_hint_y=None)
        card.bind(minimum_height=card.setter('height'))
        
        with card.canvas.before:
            Color(rgba=get_color_from_hex(bg_color) + [0.9])
            card.bg_rect = RoundedRectangle(radius=[20], pos=card.pos, size=card.size)
        
        def update_card_bg(*args):
            card.bg_rect.pos = card.pos
            card.bg_rect.size = card.size
            
        card.bind(pos=update_card_bg, size=update_card_bg)
        return card
    
    def create_setting_row(self, title, description, control_type, initial_value, callback):
        """Create a setting row with title, description and control"""
        row = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=80, padding=[10, 10])
        
        # Left side - text info
        text_layout = BoxLayout(orientation='vertical', size_hint_x=0.7)
        
        title_label = Label(
            text=title,
            font_size=20,
            color=get_color_from_hex('#ecf0f1'),
            halign='left',
            valign='bottom',
            text_size=(200, None),
            size_hint_y=None,
            height=30
        )
        text_layout.add_widget(title_label)
        
        desc_label = Label(
            text=description,
            font_size=14,
            color=get_color_from_hex('#bdc3c7'),
            halign='left',
            valign='top',
            text_size=(200, None),
            size_hint_y=None,
            height=25
        )
        text_layout.add_widget(desc_label)
        
        row.add_widget(text_layout)
        
        # Right side - control
        control_layout = AnchorLayout(size_hint_x=0.3)
        
        if control_type == 'switch':
            control = Switch(
                active=initial_value,
                size_hint=(None, None),
                size=(80, 40)
            )
            control.bind(active=callback)
        elif control_type == 'slider':
            control = Slider(
                min=10,
                max=100,
                value=initial_value,
                size_hint=(None, None),
                size=(120, 40)
            )
            control.bind(value=callback)
        
        control_layout.add_widget(control)
        row.add_widget(control_layout)
        
        return row
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
    def rgba(self, hexstr):
        c = get_color_from_hex(hexstr)
        return c if len(c) == 4 else c + [1.0] * (4 - len(c))
    
    # Setting callbacks
    def toggle_theme(self, instance, value):
        self.app.settings_manager.set('dark_theme', value)
    
    def toggle_sounds(self, instance, value):
        self.app.settings_manager.set('sounds_enabled', value)
    
    def toggle_animations(self, instance, value):
        self.app.settings_manager.set('animations_enabled', value)
    
    def toggle_autosave(self, instance, value):
        self.app.settings_manager.set('auto_save', value)
    
    def change_dice_speed(self, instance, value):
        self.app.settings_manager.set('dice_speed', int(value))
    
    def reset_character(self, instance):
        """Reset character to default values"""
        self.app.character = {
            'name': 'Mi Personaje',
            'class': 'Guerrero',
            'level': 1,
            'experience': 0,
            'hp_max': 30,
            'hp_current': 30,
            'armor': 2,
            'abilities': {
                'Fuerza': 2,
                'Destreza': 1,
                'Carisma': 0,
                'Constitución': 1,
                'Sabiduría': 0,
                'Inteligencia': -1
            },
            'thresholds': {
                'minor': 10,
                'major': 16,
                'severe': 22
            }
        }
        
        # Visual feedback
        instance.text = '✅ Reseteado'
        instance.background_color = self.rgba('#27ae60')
        Clock.schedule_once(lambda dt: self.reset_button_text(instance, '🔄 Resetear\nPersonaje'), 2)
    
    def export_character(self, instance):
        """Export character data (placeholder)"""
        import json
        
        # Save to file (simplified)
        try:
            with open('character_export.json', 'w', encoding='utf-8') as f:
                json.dump(self.app.character, f, ensure_ascii=False, indent=2)
            
            instance.text = '✅ Exportado'
            instance.background_color = self.rgba('#27ae60')
        except Exception:
            instance.text = '❌ Error'
            instance.background_color = self.rgba('#e74c3c')
        
        Clock.schedule_once(lambda dt: self.reset_button_text(instance, '📤 Exportar\nDatos'), 2)
    
    def reset_button_text(self, button, original_text):
        """Reset button to original state"""
        button.text = original_text
        button.background_color = self.rgba('#3498db')
