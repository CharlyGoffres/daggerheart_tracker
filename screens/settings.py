# screens/settings.py
"""
SettingsScreen: Allows user to view and change settings.
"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label

class SettingsScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        self.status_label = Label(text=f"Example Setting: {self.app.settings_manager.get('example_setting')}", font_size=24)
        self.layout.add_widget(self.status_label)
        self.toggle_btn = Button(text='Toggle Example Setting', font_size=28, on_release=self.toggle_setting)
        self.layout.add_widget(self.toggle_btn)
        self.layout.add_widget(Button(text='Back', font_size=28, on_release=lambda x: app.switch_screen('menu')))
        self.add_widget(self.layout)

    def toggle_setting(self, instance):
        current = self.app.settings_manager.get('example_setting', True)
        self.app.settings_manager.set('example_setting', not current)
        self.status_label.text = f"Example Setting: {not current}"
