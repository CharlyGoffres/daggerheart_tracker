"""
RollsScreen: Allows user to roll dice for abilities (2d12) and display results.
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import random

class RollsScreen(Screen):

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        Window.clearcolor = get_color_from_hex('#232946')  # Deep blue background

        main_layout = BoxLayout(orientation='vertical', spacing=10, padding=[40, 30, 40, 30])

        # Title
        title = Label(text="[b]Tiradas de Habilidad[/b]", markup=True, font_size=36, color=get_color_from_hex('#eebbc3'))
        main_layout.add_widget(title)

        # Result label
        self.result_label = Label(text="Selecciona una habilidad para tirar 2d12", font_size=24, color=get_color_from_hex('#eebbc3'))
        main_layout.add_widget(self.result_label)

        # Abilities grid
        abilities = ["Fuerza", "Destreza", "Carisma", "Constitución", "Sabiduría", "Inteligencia"]
        grid = GridLayout(cols=2, spacing=16, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        for ability in abilities:
            btn = Button(
                text=ability,
                font_size=28,
                background_color=get_color_from_hex('#eebbc3'),
                color=get_color_from_hex('#232946'),
                size_hint_y=None,
                height=70,
                on_release=self.roll_ability
            )
            grid.add_widget(btn)
        main_layout.add_widget(grid)

        # Spacer
        main_layout.add_widget(Widget(size_hint_y=0.2))

        # Back button (prominent)
        back_anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')
        back_btn = Button(
            text='⏪ Volver al Menú',
            font_size=26,
            size_hint=(None, None),
            size=(320, 60),
            background_color=get_color_from_hex('#eebbc3'),
            color=get_color_from_hex('#232946'),
            on_release=lambda x: app.switch_screen('menu')
        )
        back_anchor.add_widget(back_btn)
        main_layout.add_widget(back_anchor)

        self.add_widget(main_layout)

    def roll_ability(self, instance):
        roll1 = random.randint(1, 12)
        roll2 = random.randint(1, 12)
        total = roll1 + roll2
        # Show a popup for a more enjoyable effect
        popup_content = BoxLayout(orientation='vertical', spacing=10, padding=20)
        popup_content.add_widget(Label(text=f"[b]{instance.text}[/b]", markup=True, font_size=28, color=get_color_from_hex('#232946')))
        popup_content.add_widget(Label(text=f"🎲 {roll1} + {roll2} = [b]{total}[/b]", markup=True, font_size=36, color=get_color_from_hex('#232946')))
        close_btn = Button(text="Cerrar", size_hint=(1, 0.5), font_size=22, background_color=get_color_from_hex('#eebbc3'), color=get_color_from_hex('#232946'))
        popup_content.add_widget(close_btn)
        popup = Popup(title="Resultado de la Tirada", content=popup_content, size_hint=(None, None), size=(400, 300), auto_dismiss=False)
        close_btn.bind(on_release=popup.dismiss)
        popup.open()
        self.result_label.text = f"{instance.text}: {roll1} + {roll2} = {total}"
