"""
RollsScreen: Allows user to roll dice for abilities (2d12) and display results.
"""


from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.clock import Clock
from kivy.uix.widget import Widget
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.popup import Popup
from kivy.graphics import Color, RoundedRectangle
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
import random

class RollsScreen(Screen):

    @staticmethod
    def rgba(hexstr):
        c = get_color_from_hex(hexstr)
        return c if len(c) == 4 else c + [1.0] * (4 - len(c))

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        Window.clearcolor = get_color_from_hex('#eaf6fb')

        # Card-style container
        card = BoxLayout(orientation='vertical', spacing=12, padding=[30, 20, 30, 20], size_hint=(None, None), size=(650, 520), pos_hint={'center_x': 0.5, 'center_y': 0.5})
        with card.canvas.before:
            Color(rgba=get_color_from_hex('#ffffffcc'))
            self.bg_rect = RoundedRectangle(radius=[30], pos=card.pos, size=card.size)
        def update_bg_rect(*args):
            self.bg_rect.pos = card.pos
            self.bg_rect.size = card.size
        card.bind(pos=update_bg_rect, size=update_bg_rect)

        # Title
        title = Label(text="[b]Tiradas de Habilidad[/b]", markup=True, font_size=38, color=get_color_from_hex('#1b4965'))
        card.add_widget(title)

        # Roll type selection
        self.roll_type = Spinner(
            text='Normal',
            values=('Normal', 'Ventaja', 'Desventaja', 'Doble Ventaja', 'Triple Ventaja'),
            size_hint=(None, None),
            size=(260, 44),
            background_color=RollsScreen.rgba('#62b6cb'),
            color=RollsScreen.rgba('#1b4965'),
            font_size=22
        )
        card.add_widget(Label(text='Tipo de tirada:', font_size=20, color=get_color_from_hex('#1b4965'), size_hint_y=None, height=28))
        card.add_widget(self.roll_type)

        # Modifier selection
        self.modifier = Spinner(
            text='Sin modificador',
            values=('Sin modificador', '+1', '+2', '1d4'),
            size_hint=(None, None),
            size=(260, 44),
            background_color=RollsScreen.rgba('#97c1a9'),
            color=RollsScreen.rgba('#1b4965'),
            font_size=22
        )
        card.add_widget(Label(text='Modificador:', font_size=20, color=get_color_from_hex('#1b4965'), size_hint_y=None, height=28))
        card.add_widget(self.modifier)

        # Result label
        self.result_label = Label(text="Selecciona una habilidad para tirar 2d12", font_size=24, color=get_color_from_hex('#1b4965'))
        card.add_widget(self.result_label)


        # Dice animation area
        self.dice_label = Label(text='', font_size=48, color=RollsScreen.rgba('#1b4965'))
        card.add_widget(self.dice_label)

        # Abilities grid
        self.abilities = ["Fuerza", "Destreza", "Carisma", "Constitución", "Sabiduría", "Inteligencia"]
        grid = GridLayout(cols=2, spacing=16, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        btn_colors = ['#62b6cb', '#97c1a9', '#f3c677', '#f4978e', '#b388eb', '#ffb4a2']
        for i, ability in enumerate(self.abilities):
            btn = Button(
                text=f'🎲 {ability}',
                font_size=28,
                background_color=RollsScreen.rgba(btn_colors[i]),
                color=RollsScreen.rgba('#1b4965'),
                size_hint_y=None,
                height=70,
                on_release=self.roll_ability
            )
            grid.add_widget(btn)
        card.add_widget(grid)

        # Spacer
        card.add_widget(Widget(size_hint_y=0.2))

        # Back button (prominent)
        back_anchor = AnchorLayout(anchor_x='center', anchor_y='bottom')
        back_btn = Button(
            text='⏪ Volver al Menú',
            font_size=26,
            size_hint=(None, None),
            size=(320, 60),
            background_color=RollsScreen.rgba('#62b6cb'),
            color=RollsScreen.rgba('#ffffff'),
            on_release=lambda x: self.app.switch_screen('menu')
        )
        back_anchor.add_widget(back_btn)
        card.add_widget(back_anchor)

        # Center the card
        root = AnchorLayout()
        root.add_widget(card)
        self.add_widget(root)

    def roll_ability(self, instance):
        ability = instance.text.replace('🎲 ', '')
        mod = self.app.character.get(ability, 0)
        roll_type = self.roll_type.text
        mod_text = self.modifier.text

        # Determine number of dice and keepers for advantage/disadvantage
        if roll_type == 'Normal':
            dice = [random.randint(1, 12), random.randint(1, 12)]
        elif roll_type == 'Ventaja':
            rolls = [random.randint(1, 12), random.randint(1, 12), random.randint(1, 12)]
            dice = sorted(rolls, reverse=True)[:2]
        elif roll_type == 'Desventaja':
            rolls = [random.randint(1, 12), random.randint(1, 12), random.randint(1, 12)]
            dice = sorted(rolls)[:2]
        elif roll_type == 'Doble Ventaja':
            rolls = [random.randint(1, 12) for _ in range(4)]
            dice = sorted(rolls, reverse=True)[:2]
        elif roll_type == 'Triple Ventaja':
            rolls = [random.randint(1, 12) for _ in range(5)]
            dice = sorted(rolls, reverse=True)[:2]
        else:
            dice = [random.randint(1, 12), random.randint(1, 12)]

        # Modifier
        extra = 0
        extra_text = ''
        if mod_text == '+1':
            extra = 1
            extra_text = ' + 1'
        elif mod_text == '+2':
            extra = 2
            extra_text = ' + 2'
        elif mod_text == '1d4':
            extra = random.randint(1, 4)
            extra_text = f' + 1d4({extra})'

        # Animate dice
        self.animate_dice(dice, ability, mod, extra, extra_text)

    def animate_dice(self, dice, ability, mod, extra, extra_text):
        # Show rolling animation
        self.dice_label.text = '🎲 Rodando...'
        self.result_label.text = ''
        self._anim_frames = 12
        self._anim_count = 0
        self._final = (dice, ability, mod, extra, extra_text)
        Clock.schedule_interval(self._dice_anim_frame, 0.07)

    def _dice_anim_frame(self, dt):
        if self._anim_count < self._anim_frames:
            d1 = random.randint(1, 12)
            d2 = random.randint(1, 12)
            self.dice_label.text = f'🎲 {d1}   🎲 {d2}'
            self._anim_count += 1
            return True
        else:
            Clock.unschedule(self._dice_anim_frame)
            dice, ability, mod, extra, extra_text = self._final
            total = sum(dice) + mod + extra
            mod_str = f' + {mod}' if mod else ''
            self.dice_label.text = f'🎲 {dice[0]}   🎲 {dice[1]}'
            # Show popup with result
            popup_content = BoxLayout(orientation='vertical', spacing=10, padding=20)
            popup_content.add_widget(Label(text=f"[b]{ability}[/b]", markup=True, font_size=28, color=RollsScreen.rgba('#1b4965')))
            popup_content.add_widget(Label(text=f"🎲 {dice[0]} + {dice[1]}{mod_str}{extra_text} = [b]{total}[/b]", markup=True, font_size=36, color=RollsScreen.rgba('#1b4965')))
            close_btn = Button(text="Cerrar", size_hint=(1, 0.5), font_size=22, background_color=RollsScreen.rgba('#62b6cb'), color=RollsScreen.rgba('#ffffff'))
            popup_content.add_widget(close_btn)
            popup = Popup(title="Resultado de la Tirada", content=popup_content, size_hint=(None, None), size=(440, 320), auto_dismiss=False)
            close_btn.bind(on_release=popup.dismiss)
            popup.open()
            self.result_label.text = f"{ability}: {dice[0]} + {dice[1]}{mod_str}{extra_text} = {total}"
            return False
