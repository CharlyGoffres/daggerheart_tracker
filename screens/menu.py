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
        Window.clearcolor = get_color_from_hex('#232946')
        layout = BoxLayout(orientation='vertical', spacing=24, padding=[40, 30, 40, 30])
        # Title
        title = Label(text='[b]Daggerheart Tracker[/b]', markup=True, font_size=40, color=get_color_from_hex('#eebbc3'))
        layout.add_widget(title)
        # Buttons
        btn_style = {
            'font_size': 32,
            'background_color': get_color_from_hex('#eebbc3'),
            'color': get_color_from_hex('#232946'),
            'size_hint_y': None,
            'height': 80
        }
        layout.add_widget(Button(text='🎲 Tiradas', on_release=lambda x: app.switch_screen('rolls'), **btn_style))
        layout.add_widget(Button(text='🟢 GPIO Monitor', on_release=lambda x: app.switch_screen('gpio'), **btn_style))
        layout.add_widget(Button(text='⚙️ Ajustes', on_release=lambda x: app.switch_screen('settings'), **btn_style))
        # Exit button at the bottom
        exit_anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')
        exit_btn = Button(text='⏻ Salir', font_size=28, size_hint=(None, None), size=(220, 60), background_color=get_color_from_hex('#eebbc3'), color=get_color_from_hex('#232946'), on_release=lambda x: app.stop())
        exit_anchor.add_widget(exit_btn)
        layout.add_widget(exit_anchor)
        self.add_widget(layout)
