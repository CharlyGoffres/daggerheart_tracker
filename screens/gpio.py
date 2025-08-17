# screens/gpio.py
"""
GPIOScreen: Displays GPIO pin states.
"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from utils.gpio_helper import GPIOHelper

class GPIOScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.gpio = GPIOHelper()
        self.layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        self.status_label = Label(text='GPIO States:', font_size=24)
        self.layout.add_widget(self.status_label)
        self.refresh_btn = Button(text='Refresh', font_size=28, on_release=self.refresh)
        self.layout.add_widget(self.refresh_btn)
        self.layout.add_widget(Button(text='Back', font_size=28, on_release=lambda x: app.switch_screen('menu')))
        self.add_widget(self.layout)
        self.refresh(None)

    def refresh(self, instance):
        states = self.gpio.read_all()
        self.status_label.text = 'GPIO States:\n' + '\n'.join([f'Pin {k}: {v}' for k, v in states.items()])
