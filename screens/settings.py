# screens/settings.py
"""
SettingsScreen: Allows user to view and change settings.
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.widget import Widget
from kivy.uix.anchorlayout import AnchorLayout
from kivy.core.window import Window
from kivy.utils import get_color_from_hex

class SettingsScreen(Screen):

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
        title = Label(text='[b]Ajustes[/b]', markup=True, font_size=36, color=get_color_from_hex('#1b4965'))
        card.add_widget(title)
        # Status label
        self.status_label = Label(text=f"Ajuste de ejemplo: {self.app.settings_manager.get('example_setting')}", font_size=24, color=get_color_from_hex('#1b4965'))
        card.add_widget(self.status_label)
        # Toggle button
        self.toggle_btn = Button(text='Cambiar ajuste de ejemplo', font_size=28, background_color=get_color_from_hex('#62b6cb'), color=get_color_from_hex('#fff'), size_hint_y=None, height=70, on_release=self.toggle_setting)
        card.add_widget(self.toggle_btn)
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

    def toggle_setting(self, instance):
        current = self.app.settings_manager.get('example_setting', True)
        self.app.settings_manager.set('example_setting', not current)
        self.status_label.text = f"Example Setting: {not current}"
