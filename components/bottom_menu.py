# components/bottom_menu.py
"""
BottomMenu: Navigation bar component for the bottom of the screen
"""

from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.graphics import Color, RoundedRectangle
from kivy.utils import get_color_from_hex
from kivy.animation import Animation

class BottomMenuButton(Button):
    def __init__(self, icon, text, screen_name, app, **kwargs):
        super().__init__(**kwargs)
        self.screen_name = screen_name
        self.app = app
        self.icon = icon
        self.text_label = text
        
        # Button styling
        self.background_color = (0, 0, 0, 0)  # Transparent
        self.size_hint_y = None
        self.height = 80
        self.markup = True
        
        # Create visual elements
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#34495e'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])
        
        # Button content
        layout = BoxLayout(orientation='vertical', spacing=2, padding=5)
        
        icon_label = Label(
            text=icon,
            font_size=28,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=0.6,
            markup=True
        )
        
        text_label = Label(
            text=text,
            font_size=14,
            color=get_color_from_hex('#bdc3c7'),
            size_hint_y=0.4,
            markup=True
        )
        
        layout.add_widget(icon_label)
        layout.add_widget(text_label)
        self.add_widget(layout)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.bind(on_press=self.on_button_press)
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
    def on_button_press(self, *args):
        # Animate button press
        Animation(
            size=(self.size[0] * 0.95, self.size[1] * 0.95), 
            duration=0.1
        ).start(self)
        
        # Switch screen
        self.app.switch_screen(self.screen_name)
        
        # Reset button size
        Animation(
            size=(self.size[0] / 0.95, self.size[1] / 0.95), 
            duration=0.1
        ).start(self)
    
    def set_active(self, active=True):
        """Set button as active/inactive"""
        self.canvas.before.clear()
        with self.canvas.before:
            if active:
                Color(rgba=get_color_from_hex('#3498db'))
            else:
                Color(rgba=get_color_from_hex('#34495e'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[10])

class BottomMenu(BoxLayout):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.orientation = 'horizontal'
        self.size_hint_y = None
        self.height = 120
        self.spacing = 8
        self.padding = [15, 15, 15, 15]
        
        # Menu background
        with self.canvas.before:
            Color(rgba=get_color_from_hex('#2c3e50'))
            self.bg_rect = RoundedRectangle(pos=self.pos, size=self.size, radius=[20, 20, 0, 0])
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Menu buttons
        self.buttons = {}
        
        # Rolling dice button
        rolls_btn = BottomMenuButton(
            icon='🎲',
            text='Dados',
            screen_name='rolls',
            app=self.app
        )
        self.buttons['rolls'] = rolls_btn
        self.add_widget(rolls_btn)
        
        # Ability checks button
        ability_btn = BottomMenuButton(
            icon='🎯',
            text='Chequeos',
            screen_name='ability_checks',
            app=self.app
        )
        self.buttons['ability_checks'] = ability_btn
        self.add_widget(ability_btn)
        
        # Character screen button
        character_btn = BottomMenuButton(
            icon='⚔️',
            text='Personaje',
            screen_name='characteristics',
            app=self.app
        )
        self.buttons['characteristics'] = character_btn
        self.add_widget(character_btn)
        
        # Combat screen button
        combat_btn = BottomMenuButton(
            icon='⚡',
            text='Combate',
            screen_name='combat',
            app=self.app
        )
        self.buttons['combat'] = combat_btn
        self.add_widget(combat_btn)
        
        # Settings button
        settings_btn = BottomMenuButton(
            icon='⚙️',
            text='Ajustes',
            screen_name='settings',
            app=self.app
        )
        self.buttons['settings'] = settings_btn
        self.add_widget(settings_btn)
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
    def set_active_button(self, screen_name):
        """Update which button appears active"""
        for name, button in self.buttons.items():
            button.set_active(name == screen_name)
