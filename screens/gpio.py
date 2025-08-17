# screens/gpio.py
"""
GPIOScreen: Displays GPIO pin states.
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from utils.gpio_helper import GPIOHelper

class GPIOScreen(Screen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.gpio = GPIOHelper()
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
        title = Label(text='[b]Monitor GPIO[/b]', markup=True, font_size=36, color=get_color_from_hex('#1b4965'))
        card.add_widget(title)
        # Status label
        self.status_label = Label(text='GPIO States:', font_size=24, color=get_color_from_hex('#1b4965'))
        card.add_widget(self.status_label)
        # Refresh button
        self.refresh_btn = Button(text='Refrescar', font_size=28, background_color=get_color_from_hex('#62b6cb'), color=get_color_from_hex('#fff'), size_hint_y=None, height=70, on_release=self.refresh)
        card.add_widget(self.refresh_btn)
        # Spacer
        card.add_widget(Widget(size_hint_y=0.2))
        # Back button
        back_anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')
        back_btn = Button(text='⏪ Volver al Menú', font_size=26, size_hint=(None, None), size=(320, 60), background_color=get_color_from_hex('#f4978e'), color=get_color_from_hex('#fff'), on_release=lambda x: app.switch_screen('menu'))
        back_anchor.add_widget(back_btn)
        card.add_widget(back_anchor)
        # Center the card
        root = AnchorLayout()
        root.add_widget(card)
        self.add_widget(root)
        self.refresh(None)

    def refresh(self, instance):
        states = self.gpio.read_all()
        self.status_label.text = 'GPIO States:\n' + '\n'.join([f'Pin {k}: {v}' for k, v in states.items()])
