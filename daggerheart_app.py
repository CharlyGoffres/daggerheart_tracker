import tkinter as tk
import random

class DaggerheartApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Daggerheart App")
        self.geometry("800x480")  # Pantalla típica Raspberry
        self.current_frame = None

        # Dades del personatge (es poden editar)
        self.hp = 30
        self.max_hp = 30
        self.armor = 12
        self.spell_slots = 3
        self.weapons = {"Espada": (1, 8), "Arco": (1, 6)}
        self.spells = {"Fuego": (2, 6)}

        self.show_main_menu()

    def switch_frame(self, frame_class):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = frame_class(self)
        self.current_frame.pack(fill="both", expand=True)

    def show_main_menu(self):
        self.switch_frame(MainMenu)


# ------------------- MENÚ PRINCIPAL -------------------
class MainMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Menú Principal", font=("Arial", 24)).pack(pady=20)

        tk.Button(self, text="Tiradas", font=("Arial", 18),
                  command=lambda: master.switch_frame(RollsMenu)).pack(pady=10)

        tk.Button(self, text="Ficha", font=("Arial", 18),
                  command=lambda: master.switch_frame(CharacterSheet)).pack(pady=10)

        tk.Button(self, text="Combate", font=("Arial", 18),
                  command=lambda: master.switch_frame(CombatMenu)).pack(pady=10)

        tk.Button(self, text="Editor", font=("Arial", 18),
                  command=lambda: master.switch_frame(EditorMenu)).pack(pady=10)


# ------------------- MENÚ DE TIRADAS -------------------
class RollsMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Tiradas de Habilidad (2d12)", font=("Arial", 20)).pack(pady=20)

        self.result_label = tk.Label(self, text="", font=("Arial", 18))
        self.result_label.pack(pady=10)

        for habilidad in ["Fuerza", "Destreza", "Carisma", "Constitución", "Sabiduría", "Inteligencia"]:
            tk.Button(self, text=habilidad, font=("Arial", 16),
                      command=lambda h=habilidad: self.roll_dice(h)).pack(pady=5)

        tk.Button(self, text="Volver", font=("Arial", 16),
                  command=master.show_main_menu).pack(pady=20)

    def roll_dice(self, habilidad):
        d1 = random.randint(1, 12)
        d2 = random.randint(1, 12)
        total = d1 + d2
        self.result_label.config(text=f"{habilidad}: {d1} + {d2} = {total}")


# ------------------- FICHA -------------------
class CharacterSheet(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Ficha de Personaje", font=("Arial", 20)).pack(pady=20)

        self.hp_label = tk.Label(self, text=f"HP: {master.hp}/{master.max_hp}", font=("Arial", 16))
        self.hp_label.pack(pady=5)
        tk.Label(self, text=f"Armadura: {master.armor}", font=("Arial", 16)).pack(pady=5)
        tk.Label(self, text=f"Spell Slots: {master.spell_slots}", font=("Arial", 16)).pack(pady=5)

        tk.Button(self, text="Volver", font=("Arial", 16),
                  command=master.show_main_menu).pack(pady=20)


# ------------------- COMBATE -------------------
class CombatMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Combate", font=("Arial", 20)).pack(pady=20)

        self.hp_label = tk.Label(self, text=f"HP: {master.hp}/{master.max_hp}", font=("Arial", 18))
        self.hp_label.pack(pady=10)

        tk.Button(self, text="-1 HP", font=("Arial", 16),
                  command=lambda: self.modify_hp(master, -1)).pack(pady=5)
        tk.Button(self, text="+1 HP", font=("Arial", 16),
                  command=lambda: self.modify_hp(master, +1)).pack(pady=5)

        self.result_label = tk.Label(self, text="", font=("Arial", 18))
        self.result_label.pack(pady=10)

        tk.Label(self, text="Armas:", font=("Arial", 16)).pack(pady=10)
        for weapon, (n, faces) in master.weapons.items():
            tk.Button(self, text=f"{weapon} ({n}d{faces})", font=("Arial", 16),
                      command=lambda w=weapon: self.attack(master, w)).pack(pady=5)

        tk.Label(self, text="Hechizos:", font=("Arial", 16)).pack(pady=10)
        for spell, (n, faces) in master.spells.items():
            tk.Button(self, text=f"{spell} ({n}d{faces})", font=("Arial", 16),
                      command=lambda s=spell: self.cast_spell(master, s)).pack(pady=5)

        tk.Button(self, text="Volver", font=("Arial", 16),
                  command=master.show_main_menu).pack(pady=20)

    def modify_hp(self, master, amount):
        master.hp = max(0, min(master.max_hp, master.hp + amount))
        self.hp_label.config(text=f"HP: {master.hp}/{master.max_hp}")

    def attack(self, master, weapon):
        n, faces = master.weapons[weapon]
        rolls = [random.randint(1, faces) for _ in range(n)]
        total = sum(rolls)
        self.result_label.config(text=f"Ataque con {weapon}: {rolls} = {total}")

    def cast_spell(self, master, spell):
        n, faces = master.spells[spell]
        rolls = [random.randint(1, faces) for _ in range(n)]
        total = sum(rolls)
        self.result_label.config(text=f"{spell}: {rolls} = {total}")


# ------------------- EDITOR -------------------
class EditorMenu(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="Editor de Personaje", font=("Arial", 20)).pack(pady=20)

        # Vida
        tk.Label(self, text="HP Máximo:", font=("Arial", 14)).pack()
        self.hp_entry = tk.Entry(self)
        self.hp_entry.insert(0, str(master.max_hp))
        self.hp_entry.pack()

        # Armadura
        tk.Label(self, text="Armadura:", font=("Arial", 14)).pack()
        self.armor_entry = tk.Entry(self)
        self.armor_entry.insert(0, str(master.armor))
        self.armor_entry.pack()

        # Spell slots
        tk.Label(self, text="Spell Slots:", font=("Arial", 14)).pack()
        self.slots_entry = tk.Entry(self)
        self.slots_entry.insert(0, str(master.spell_slots))
        self.slots_entry.pack()

        tk.Button(self, text="Guardar", font=("Arial", 16),
                  command=lambda: self.save(master)).pack(pady=20)
        tk.Button(self, text="Volver", font=("Arial", 16),
                  command=master.show_main_menu).pack()

    def save(self, master):
        master.max_hp = int(self.hp_entry.get())
        master.hp = master.max_hp
        master.armor = int(self.armor_entry.get())
        master.spell_slots = int(self.slots_entry.get())
        tk.Label(self, text="¡Datos actualizados!", font=("Arial", 14), fg="green").pack()

# ------------------- MAIN -------------------
if __name__ == "__main__":
    app = DaggerheartApp()
    app.mainloop()
