# screens/menu.py
"""
MenuScreen: Main menu with navigation buttons.
"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button

class MenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        layout.add_widget(Button(text='Rolls (Tiradas)', font_size=32, on_release=lambda x: app.switch_screen('rolls')))
        layout.add_widget(Button(text='GPIO Monitor', font_size=32, on_release=lambda x: app.switch_screen('gpio')))
        layout.add_widget(Button(text='Settings', font_size=32, on_release=lambda x: app.switch_screen('settings')))
        layout.add_widget(Button(text='Exit', font_size=32, on_release=lambda x: app.stop()))
        self.add_widget(layout)
