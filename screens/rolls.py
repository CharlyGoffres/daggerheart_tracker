"""
RollsScreen: Allows user to roll dice for abilities (2d12) and display results.
"""
from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
import random

class RollsScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.layout = BoxLayout(orientation='vertical', spacing=20, padding=40)
        self.result_label = Label(text="Select an ability to roll (2d12)", font_size=24)
        self.layout.add_widget(self.result_label)
        abilities = ["Fuerza", "Destreza", "Carisma", "Constitución", "Sabiduría", "Inteligencia"]
        for ability in abilities:
            btn = Button(text=ability, font_size=28, on_release=self.roll_ability)
            self.layout.add_widget(btn)
        self.layout.add_widget(Button(text='Back', font_size=28, on_release=lambda x: app.switch_screen('menu')))
        self.add_widget(self.layout)

    def roll_ability(self, instance):
        roll1 = random.randint(1, 12)
        roll2 = random.randint(1, 12)
        total = roll1 + roll2
        self.result_label.text = f"{instance.text}: {roll1} + {roll2} = {total}"
