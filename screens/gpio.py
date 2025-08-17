# screens/gpio.py
"""
GPIOScreen: Displays GPIO pin states.
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from utils.gpio_helper import GPIOHelper

class GPIOScreen(Screen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.gpio = GPIOHelper()
        Window.clearcolor = get_color_from_hex('#232946')
        layout = BoxLayout(orientation='vertical', spacing=24, padding=[40, 30, 40, 30])
        # Title
        title = Label(text='[b]Monitor GPIO[/b]', markup=True, font_size=36, color=get_color_from_hex('#eebbc3'))
        layout.add_widget(title)
        # Status label
        self.status_label = Label(text='GPIO States:', font_size=24, color=get_color_from_hex('#eebbc3'))
        layout.add_widget(self.status_label)
        # Refresh button
        self.refresh_btn = Button(text='Refrescar', font_size=28, background_color=get_color_from_hex('#eebbc3'), color=get_color_from_hex('#232946'), size_hint_y=None, height=70, on_release=self.refresh)
        layout.add_widget(self.refresh_btn)
        # Spacer
        layout.add_widget(Label(size_hint_y=0.2))
        # Back button
        back_anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')
        back_btn = Button(text='⏪ Volver al Menú', font_size=26, size_hint=(None, None), size=(320, 60), background_color=get_color_from_hex('#eebbc3'), color=get_color_from_hex('#232946'), on_release=lambda x: app.switch_screen('menu'))
        back_anchor.add_widget(back_btn)
        layout.add_widget(back_anchor)
        self.add_widget(layout)
        self.refresh(None)

    def refresh(self, instance):
        states = self.gpio.read_all()
        self.status_label.text = 'GPIO States:\n' + '\n'.join([f'Pin {k}: {v}' for k, v in states.items()])
