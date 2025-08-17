# screens/settings.py
"""
SettingsScreen: Allows user to view and change settings.
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SettingsScreen(Screen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        Window.clearcolor = get_color_from_hex('#232946')
        layout = BoxLayout(orientation='vertical', spacing=24, padding=[40, 30, 40, 30])
        # Title
        title = Label(text='[b]Ajustes[/b]', markup=True, font_size=36, color=get_color_from_hex('#eebbc3'))
        layout.add_widget(title)
        # Status label
        self.status_label = Label(text=f"Ajuste de ejemplo: {self.app.settings_manager.get('example_setting')}", font_size=24, color=get_color_from_hex('#eebbc3'))
        layout.add_widget(self.status_label)
        # Toggle button
        self.toggle_btn = Button(text='Cambiar ajuste de ejemplo', font_size=28, background_color=get_color_from_hex('#eebbc3'), color=get_color_from_hex('#232946'), size_hint_y=None, height=70, on_release=self.toggle_setting)
        layout.add_widget(self.toggle_btn)
        # Spacer
        layout.add_widget(Label(size_hint_y=0.2))
        # Back button
        back_anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')
        back_btn = Button(text='⏪ Volver al Menú', font_size=26, size_hint=(None, None), size=(320, 60), background_color=get_color_from_hex('#eebbc3'), color=get_color_from_hex('#232946'), on_release=lambda x: app.switch_screen('menu'))
        back_anchor.add_widget(back_btn)
        layout.add_widget(back_anchor)
        self.add_widget(layout)

    def toggle_setting(self, instance):
        current = self.app.settings_manager.get('example_setting', True)
        self.app.settings_manager.set('example_setting', not current)
        self.status_label.text = f"Example Setting: {not current}"
