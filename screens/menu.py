# screens/menu.py
"""
MenuScreen: Main menu with navigation buttons.
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class MenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        Window.clearcolor = get_color_from_hex('#eaf6fb')
        # Card-style container
        card = BoxLayout(orientation='vertical', spacing=24, padding=[30, 30, 30, 30], size_hint=(None, None), size=(500, 420), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        from kivy.graphics import Color, RoundedRectangle
        with card.canvas.before:
            Color(rgba=get_color_from_hex('#ffffffcc'))
            self.bg_rect = RoundedRectangle(radius=[30], pos=card.pos, size=card.size)
        def update_bg_rect(*args):
            self.bg_rect.pos = card.pos
            self.bg_rect.size = card.size
        card.bind(pos=update_bg_rect, size=update_bg_rect)
        # Title
        title = Label(text='[b]Daggerheart Tracker[/b]', markup=True, font_size=40, color=get_color_from_hex('#1b4965'))
        card.add_widget(title)
        # Buttons
        def rgba(hexstr):
            c = get_color_from_hex(hexstr)
            return c if len(c) == 4 else c + [1.0] * (4 - len(c))
        btn_style = {
            'font_size': 32,
            'background_color': rgba('#62b6cb'),
            'color': rgba('#ffffff'),
            'size_hint_y': None,
            'height': 80
        }
        card.add_widget(Button(text='🎲 Tiradas', on_release=lambda x: app.switch_screen('rolls'), **btn_style))
        card.add_widget(Button(text='🟢 GPIO Monitor', on_release=lambda x: app.switch_screen('gpio'), **btn_style))
        card.add_widget(Button(text='⚙️ Ajustes', on_release=lambda x: app.switch_screen('settings'), **btn_style))
        # Exit button at the bottom
        exit_anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')
        exit_btn = Button(text='⏻ Salir', font_size=28, size_hint=(None, None), size=(220, 60), background_color=rgba('#f4978e'), color=rgba('#ffffff'), on_release=lambda x: app.stop())
        exit_anchor.add_widget(exit_btn)
        card.add_widget(exit_anchor)
        # Center the card
        root = AnchorLayout()
        root.add_widget(card)
        self.add_widget(root)
