"""
RollsScreen: Modern dice rolling interface with beautiful animations and responsive design
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
from kivy.uix.scrollview import ScrollView
from kivy.graphics import Color, RoundedRectangle, Line
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.animation import Animation
from components.bottom_menu_fixed import FixedBottomMenu
from components.modern_button import ModernButton, ModernActionButton, ModernDangerButton, ModernSuccessButton
from components.responsive_utils import ResponsiveUtils
from components.responsive_layout import ResponsiveBoxLayout, ResponsiveGridLayout
from components.layout_utils import LayoutUtils
import random

class RollsScreen(Screen):

    @staticmethod
    def rgba(hexstr):
        c = get_color_from_hex(hexstr)
        return c if len(c) == 4 else c + [1.0] * (4 - len(c))
    
    @staticmethod
    def darken_color(hex_color, factor=0.8):
        """Darken a hex color by a factor"""
        color = get_color_from_hex(hex_color)
        return f"#{int(color[0]*255*factor):02x}{int(color[1]*255*factor):02x}{int(color[2]*255*factor):02x}"

    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        # Create beautiful gradient background like the menu
        LayoutUtils.create_gradient_background(self, '#ff9a9e', '#fecfef')
        
        # Create main container with standardized layout
        scroll, main_layout = LayoutUtils.create_scrollable_content()
        main_container, self.bottom_menu = LayoutUtils.create_main_container(
            self.app, scroll, FixedBottomMenu
        )
        
        self.add_widget(main_container)
        
        # Create centered header
        header, title = LayoutUtils.create_centered_header('[b]🎲 TIRADAS DE DADOS[/b]')
        main_layout.add_widget(header)

        # Configuration card with enhanced styling
        config_card = self.create_card('#34495e')
        config_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        config_title = Label(
            text='[b]Configuración de Tirada[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        config_layout.add_widget(config_title)

        # Roll type selection with modern styling
        roll_type_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        roll_type_layout.add_widget(Label(
            text='Tipo:', 
            font_size=18, 
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.3
        ))
        
        self.roll_type = Spinner(
            text='Normal',
            values=('Normal', 'Ventaja', 'Desventaja', 'Doble Ventaja', 'Triple Ventaja'),
            size_hint_x=0.7,
            background_color=RollsScreen.rgba('#3498db'),
            color=RollsScreen.rgba('#ffffff'),
            font_size=18
        )
        roll_type_layout.add_widget(self.roll_type)
        config_layout.add_widget(roll_type_layout)

        # Modifier selection
        modifier_layout = BoxLayout(orientation='horizontal', spacing=15, size_hint_y=None, height=50)
        modifier_layout.add_widget(Label(
            text='Modificador:', 
            font_size=18, 
            color=get_color_from_hex('#bdc3c7'),
            size_hint_x=0.3
        ))
        
        self.modifier = Spinner(
            text='Sin modificador',
            values=('Sin modificador', '+1', '+2', '1d4'),
            size_hint_x=0.7,
            background_color=RollsScreen.rgba('#27ae60'),
            color=RollsScreen.rgba('#ffffff'),
            font_size=18
        )
        modifier_layout.add_widget(self.modifier)
        config_layout.add_widget(modifier_layout)
        
        config_card.add_widget(config_layout)
        main_layout.add_widget(config_card)

        # Results display card
        results_card = self.create_card('#2c3e50')
        results_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        self.result_label = Label(
            text='Selecciona una habilidad para comenzar',
            font_size=20,
            color=get_color_from_hex('#ecf0f1'),
            halign='center',
            valign='middle',
            text_size=(None, None),
            markup=True
        )
        results_layout.add_widget(self.result_label)

        # Animated dice display
        self.dice_label = Label(
            text='🎲 🎲',
            font_size=64,
            color=RollsScreen.rgba('#f39c12'),
            halign='center',
            valign='middle',
            text_size=(None, None)
        )
        results_layout.add_widget(self.dice_label)
        
        results_card.add_widget(results_layout)
        main_layout.add_widget(results_card)

        # Abilities grid with beautiful cards
        abilities_card = self.create_card('#34495e')
        abilities_layout = BoxLayout(orientation='vertical', spacing=15, padding=20)
        
        abilities_title = Label(
            text='[b]Habilidades del Personaje[/b]',
            markup=True,
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            size_hint_y=None,
            height=40
        )
        abilities_layout.add_widget(abilities_title)
        
        # Create responsive grid with better spacing
        grid = ResponsiveGridLayout(auto_cols=True, size_hint_y=None)
        grid.bind(minimum_height=grid.setter('height'))
        
        self.abilities = ["Fuerza", "Destreza", "Carisma", "Constitución", "Sabiduría", "Inteligencia"]
        btn_colors = ['#e74c3c', '#3498db', '#9b59b6', '#e67e22', '#27ae60', '#f39c12']
        
        for i, ability in enumerate(self.abilities):
            ability_mod = self.app.character['abilities'].get(ability, 0)
            mod_text = f"{ability_mod:+d}" if ability_mod != 0 else "0"
            
            btn = self.create_ability_button(
                f'{ability}\n({mod_text})',
                btn_colors[i],
                self.roll_ability
            )
            grid.add_widget(btn)
        
        abilities_layout.add_widget(grid)
        abilities_card.add_widget(abilities_layout)
        main_layout.add_widget(abilities_card)

        # Bind responsive updates
        LayoutUtils.bind_responsive_updates(main_layout, title)
    
    def on_enter(self):
        """Called when entering the screen"""
        super().on_enter()
        self.bottom_menu.set_active_button('rolls')
    
    def on_window_resize(self, *args):
        """Called when window is resized"""
        # This will trigger responsive updates in all responsive components
        pass
    
    def create_card(self, bg_color):
        """Create a modern card container"""
        card = BoxLayout(orientation='vertical')
        with card.canvas.before:
            Color(rgba=get_color_from_hex(bg_color) + [0.9])
            card.card_rect = RoundedRectangle(radius=[20], pos=card.pos, size=card.size)
        
        def update_card_bg(*args):
            card.card_rect.pos = card.pos
            card.card_rect.size = card.size
            
        card.bind(pos=update_card_bg, size=update_card_bg)
        return card
    
    def create_ability_button(self, text, color, callback):
        """Create a modern ability button with hover effects"""
        btn = ModernActionButton(
            text=text,
            font_size=18,
            size_hint_y=None,
            height=90,  # Increased height for better spacing
            halign='center',
            valign='middle',
            on_release=callback,
            bg_color=color,
            hover_color=self.darken_color(color)
        )
        
        # Ensure text wraps properly
        btn.bind(size=btn.setter('text_size'))
        
        return btn

    def roll_ability(self, instance):
        print(f"Rolling ability: {instance.text}")  # Debug output
        # Extract ability name from button text
        ability_text = instance.text.split('\n')[0]  # Get first line before modifier
        mod = self.app.character['abilities'].get(ability_text, 0)
        roll_type = self.roll_type.text
        mod_text = self.modifier.text

        print(f"Ability: {ability_text}, Modifier: {mod}, Roll type: {roll_type}")  # Debug output

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

        # Animate dice with enhanced visuals
        self.animate_dice(dice, ability_text, mod, extra, extra_text)

    def animate_dice(self, dice, ability, mod, extra, extra_text):
        # Enhanced rolling animation with color changes
        self.dice_label.text = '🎲 Rodando... 🎲'
        self.dice_label.color = RollsScreen.rgba('#f39c12')
        self.result_label.text = f'Tirando {ability}...'
        
        # Create rolling animation
        self._anim_frames = 15
        self._anim_count = 0
        self._final = (dice, ability, mod, extra, extra_text)
        Clock.schedule_interval(self._dice_anim_frame, 0.08)

    def _dice_anim_frame(self, dt):
        if self._anim_count < self._anim_frames:
            d1 = random.randint(1, 12)
            d2 = random.randint(1, 12)
            
            # Change color during animation
            colors = ['#e74c3c', '#f39c12', '#27ae60', '#3498db', '#9b59b6']
            color = colors[self._anim_count % len(colors)]
            self.dice_label.color = RollsScreen.rgba(color)
            self.dice_label.text = f'🎲 {d1}   🎲 {d2}'
            
            self._anim_count += 1
            return True
        else:
            Clock.unschedule(self._dice_anim_frame)
            dice, ability, mod, extra, extra_text = self._final
            total = sum(dice) + mod + extra
            mod_str = f' + {mod}' if mod else ''
            
            # Final result with success indication
            result_color = '#27ae60' if total >= 15 else '#e74c3c' if total <= 9 else '#f39c12'
            self.dice_label.color = RollsScreen.rgba(result_color)
            self.dice_label.text = f'🎲 {dice[0]}   🎲 {dice[1]}'
            
            # Show enhanced popup with result analysis
            self.show_result_popup(ability, dice, mod, extra, extra_text, total)
            
            # Update result display
            success_text = ""
            if total >= self.app.character['thresholds']['severe']:
                success_text = " [color=#27ae60](ÉXITO CRÍTICO!)[/color]"
            elif total >= self.app.character['thresholds']['major']:
                success_text = " [color=#27ae60](Éxito Mayor)[/color]"
            elif total >= self.app.character['thresholds']['minor']:
                success_text = " [color=#f39c12](Éxito Menor)[/color]"
            else:
                success_text = " [color=#e74c3c](Fallo)[/color]"
            
            self.result_label.text = f"[b]{ability}[/b]: {dice[0]} + {dice[1]}{mod_str}{extra_text} = [b]{total}[/b]{success_text}"
            self.result_label.markup = True
            return False
    
    def show_result_popup(self, ability, dice, mod, extra, extra_text, total):
        """Show an enhanced result popup with beautiful styling"""
        popup_content = BoxLayout(orientation='vertical', spacing=20, padding=30)
        
        # Background
        with popup_content.canvas.before:
            Color(rgba=get_color_from_hex('#2c3e50'))
            popup_content.bg_rect = RoundedRectangle(radius=[20], pos=popup_content.pos, size=popup_content.size)
        
        popup_content.bind(pos=lambda *args: setattr(popup_content.bg_rect, 'pos', popup_content.pos),
                          size=lambda *args: setattr(popup_content.bg_rect, 'size', popup_content.size))
        
        # Title
        title_label = Label(
            text=f"[b]💫 {ability} 💫[/b]",
            markup=True,
            font_size=32,
            color=RollsScreen.rgba('#ecf0f1')
        )
        popup_content.add_widget(title_label)
        
        # Dice result
        mod_str = f' + {mod}' if mod else ''
        dice_label = Label(
            text=f"🎲 {dice[0]} + {dice[1]}{mod_str}{extra_text}",
            font_size=24,
            color=RollsScreen.rgba('#f39c12')
        )
        popup_content.add_widget(dice_label)
        
        # Total with styling
        total_label = Label(
            text=f"[b]TOTAL: {total}[/b]",
            markup=True,
            font_size=36,
            color=RollsScreen.rgba('#e74c3c' if total <= 9 else '#f39c12' if total < 15 else '#27ae60')
        )
        popup_content.add_widget(total_label)
        
        # Success indicator
        if total >= self.app.character['thresholds']['severe']:
            success_label = Label(text="🌟 ÉXITO CRÍTICO! 🌟", font_size=24, color=RollsScreen.rgba('#27ae60'))
        elif total >= self.app.character['thresholds']['major']:
            success_label = Label(text="⭐ Éxito Mayor ⭐", font_size=20, color=RollsScreen.rgba('#27ae60'))
        elif total >= self.app.character['thresholds']['minor']:
            success_label = Label(text="✨ Éxito Menor ✨", font_size=18, color=RollsScreen.rgba('#f39c12'))
        else:
            success_label = Label(text="💥 Fallo 💥", font_size=18, color=RollsScreen.rgba('#e74c3c'))
        
        popup_content.add_widget(success_label)
        
        # Close button
        close_btn = ModernSuccessButton(
            text="✅ Cerrar",
            size_hint=(None, None),
            size=(200, 60),
            font_size=20
        )
        
        popup_content.add_widget(close_btn)
        
        popup = Popup(
            title="",
            content=popup_content,
            size_hint=(None, None),
            size=(500, 400),
            auto_dismiss=False,
            separator_height=0
        )
        
        close_btn.bind(on_release=popup.dismiss)
        popup.open()
