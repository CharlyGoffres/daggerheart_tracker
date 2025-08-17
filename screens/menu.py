# screens/menu.py
"""
MenuScreen: Beautiful, modern main menu with Material Design elements
"""

from kivy.uix.screenmanager import Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.graphics import Color, RoundedRectangle, Ellipse
from kivy.animation import Animation
from kivy.clock import Clock
from components.bottom_menu import BottomMenu

class ModernButton(Button):
    def __init__(self, bg_color='#3498db', hover_color='#2980b9', **kwargs):
        super().__init__(**kwargs)
        self.bg_color = get_color_from_hex(bg_color)
        self.hover_color = get_color_from_hex(hover_color)
        self.normal_color = self.bg_color[:]
        self.background_color = (0, 0, 0, 0)  # Transparent
        
        with self.canvas.before:
            Color(rgba=self.bg_color)
            self.bg_rect = RoundedRectangle(radius=[15], pos=self.pos, size=self.size)
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        self.bind(on_press=self.on_button_press)
        self.bind(on_release=self.on_button_release)
    
    def update_bg(self, *args):
        self.bg_rect.pos = self.pos
        self.bg_rect.size = self.size
    
    def on_button_press(self, *args):
        Animation(bg_color=self.hover_color, duration=0.1).start(self)
        Animation(size=(self.size[0] * 0.95, self.size[1] * 0.95), duration=0.1).start(self)
    
    def on_button_release(self, *args):
        Animation(bg_color=self.normal_color, duration=0.1).start(self)
        Animation(size=(self.size[0] / 0.95, self.size[1] / 0.95), duration=0.1).start(self)

class MenuScreen(Screen):
    def __init__(self, app, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        
        # Create gradient background
        with self.canvas.before:
            # Top gradient color
            Color(rgba=get_color_from_hex('#667eea'))
            self.bg_gradient_top = RoundedRectangle(pos=self.pos, size=(self.size[0], self.size[1] * 0.6))
            
            # Bottom gradient color 
            Color(rgba=get_color_from_hex('#764ba2'))
            self.bg_gradient_bottom = RoundedRectangle(pos=(self.pos[0], self.pos[1] + self.size[1] * 0.4), 
                                                     size=(self.size[0], self.size[1] * 0.6))
        
        self.bind(pos=self.update_bg, size=self.update_bg)
        
        # Main container with bottom menu
        main_container = BoxLayout(orientation='vertical')
        
        # Main content container
        main_layout = BoxLayout(orientation='vertical', padding=[40, 60, 40, 20], spacing=30)
        
        # Header section
        header = BoxLayout(orientation='vertical', size_hint_y=0.3, spacing=20)
        
        # App title with shadow effect
        title_container = AnchorLayout()
        title = Label(
            text='[b]DAGGERHEART[/b]\n[color=#f1c40f]⚔️ TRACKER ⚔️[/color]',
            markup=True,
            font_size=56,
            color=get_color_from_hex('#ffffff'),
            halign='center',
            valign='middle',
            text_size=(None, None)
        )
        title_container.add_widget(title)
        header.add_widget(title_container)
        
        # Subtitle
        subtitle = Label(
            text='Tu compañero de aventuras definitivo',
            font_size=24,
            color=get_color_from_hex('#ecf0f1'),
            halign='center'
        )
        header.add_widget(subtitle)
        
        main_layout.add_widget(header)
        
        # Navigation cards
        nav_container = BoxLayout(orientation='vertical', size_hint_y=0.6, spacing=20)
        
        # Create navigation buttons with icons and descriptions
        nav_buttons = [
            {
                'title': '🎲 Tiradas de Dados',
                'subtitle': 'Realiza tiradas con ventajas y modificadores',
                'color': '#e74c3c',
                'screen': 'rolls'
            },
            {
                'title': '⚔️ Ficha de Personaje', 
                'subtitle': 'Gestiona stats, vida y habilidades',
                'color': '#27ae60',
                'screen': 'characteristics'
            },
            {
                'title': '⚙️ Configuración',
                'subtitle': 'Personaliza tu experiencia',
                'color': '#8e44ad',
                'screen': 'settings'
            }
        ]
        
        for btn_data in nav_buttons:
            nav_card = self.create_nav_card(
                btn_data['title'],
                btn_data['subtitle'], 
                btn_data['color'],
                lambda x, screen=btn_data['screen']: self.app.switch_screen(screen, 'left')
            )
            nav_container.add_widget(nav_card)
        
        main_layout.add_widget(nav_container)
        
        # Footer with exit button
        footer = AnchorLayout(size_hint_y=0.1)
        exit_btn = ModernButton(
            text='💀 Salir del Juego',
            font_size=18,
            size_hint=(None, None),
            size=(200, 50),
            bg_color='#c0392b',
            hover_color='#a93226',
            color=get_color_from_hex('#ffffff'),
            on_release=lambda x: self.app.stop()
        )
        footer.add_widget(exit_btn)
        main_layout.add_widget(footer)
        
        main_container.add_widget(main_layout)
        
        # Add bottom menu
        self.bottom_menu = BottomMenu(self.app)
        main_container.add_widget(self.bottom_menu)
        
        self.add_widget(main_container)
    
    def on_enter(self):
        """Called when entering the screen"""
        super().on_enter()
        if hasattr(self, 'bottom_menu'):
            # Don't highlight any button on the main menu
            for button in self.bottom_menu.buttons.values():
                button.set_active(False)
    
    def create_nav_card(self, title, subtitle, color, callback):
        """Create a modern navigation card"""
        card_container = AnchorLayout(size_hint_y=None, height=100)
        card = BoxLayout(orientation='horizontal', spacing=20, padding=[20, 10])
        
        # Card background
        with card.canvas.before:
            Color(rgba=get_color_from_hex('#ffffff') + [0.95])
            card.bg_rect = RoundedRectangle(radius=[20], pos=card.pos, size=card.size)
        
        def update_card_bg(*args):
            card.bg_rect.pos = card.pos
            card.bg_rect.size = card.size
        
        card.bind(pos=update_card_bg, size=update_card_bg)
        
        # Icon section
        icon_section = AnchorLayout(size_hint_x=0.2)
        with icon_section.canvas.before:
            Color(rgba=get_color_from_hex(color))
            icon_section.icon_bg = RoundedRectangle(radius=[15], pos=(0, 0), size=(60, 60))
        
        # Content section
        content = BoxLayout(orientation='vertical', size_hint_x=0.8, padding=[20, 15, 10, 15], spacing=5)
        
        title_label = Label(
            text=title,
            font_size=22,
            color=get_color_from_hex('#2c3e50'),
            halign='left',
            valign='bottom',
            text_size=(300, None),
            markup=True,
            size_hint_y=0.6
        )
        
        subtitle_label = Label(
            text=subtitle,
            font_size=16,
            color=get_color_from_hex('#7f8c8d'),
            halign='left',
            valign='top',
            text_size=(300, None),
            size_hint_y=0.4
        )
        
        content.add_widget(title_label)
        content.add_widget(subtitle_label)
        
        card.add_widget(icon_section)
        card.add_widget(content)
        
        # Make the whole card clickable
        button_overlay = Button(
            background_color=(0, 0, 0, 0),
            on_release=callback
        )
        
        card_container.add_widget(card)
        card_container.add_widget(button_overlay)
        
        return card_container
    
    def update_bg(self, *args):
        self.bg_gradient_top.pos = self.pos
        self.bg_gradient_top.size = (self.size[0], self.size[1] * 0.6)
        self.bg_gradient_bottom.pos = (self.pos[0], self.pos[1] + self.size[1] * 0.4)
        self.bg_gradient_bottom.size = (self.size[0], self.size[1] * 0.6)
