"""
Character Model for Qt/QML Version
Manages character data with Qt properties and signals
"""

from PySide6.QtCore import QObject, Signal, Property

class CharacterModel(QObject):
    """Character data model with Qt properties"""
    
    # Signals for property changes
    nameChanged = Signal()
    classNameChanged = Signal()
    levelChanged = Signal()
    hpCurrentChanged = Signal()
    hpMaxChanged = Signal()
    armorChanged = Signal()
    abilitiesChanged = Signal()
    hopeChanged = Signal()
    fearChanged = Signal()
    
    def __init__(self):
        super().__init__()
        
        # Character basic info
        self._name = "Mi Personaje"
        self._class_name = "Guerrero"
        self._level = 1
        
        # Health and defense
        self._hp_current = 30
        self._hp_max = 30
        self._armor = 2
        
        # Resources
        self._hope = 1
        self._fear = 0
        
        # Abilities
        self._abilities = {
            "Fuerza": 2,
            "Destreza": 1,
            "Carisma": 0,
            "Constitución": 1,
            "Sabiduría": 0,
            "Inteligencia": -1
        }
        
        # Thresholds
        self._thresholds = {
            "minor": 10,
            "major": 16,
            "severe": 22
        }
    
    # Name property
    @Property(str, notify=nameChanged)
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if self._name != value:
            self._name = value
            self.nameChanged.emit()
    
    # Class name property
    @Property(str, notify=classNameChanged)
    def className(self):
        return self._class_name
    
    @className.setter
    def className(self, value):
        if self._class_name != value:
            self._class_name = value
            self.classNameChanged.emit()
    
    # Level property
    @Property(int, notify=levelChanged)
    def level(self):
        return self._level
    
    @level.setter
    def level(self, value):
        if self._level != value:
            self._level = value
            self.levelChanged.emit()
    
    # Current HP property
    @Property(int, notify=hpCurrentChanged)
    def hpCurrent(self):
        return self._hp_current
    
    @hpCurrent.setter
    def hpCurrent(self, value):
        if self._hp_current != value:
            self._hp_current = max(0, min(self._hp_max, value))
            self.hpCurrentChanged.emit()
    
    # Max HP property
    @Property(int, notify=hpMaxChanged)
    def hpMax(self):
        return self._hp_max
    
    @hpMax.setter
    def hpMax(self, value):
        if self._hp_max != value:
            self._hp_max = value
            self.hpMaxChanged.emit()
    
    # Armor property
    @Property(int, notify=armorChanged)
    def armor(self):
        return self._armor
    
    @armor.setter
    def armor(self, value):
        if self._armor != value:
            self._armor = value
            self.armorChanged.emit()
    
    # Hope property
    @Property(int, notify=hopeChanged)
    def hope(self):
        return self._hope
    
    @hope.setter
    def hope(self, value):
        if self._hope != value:
            self._hope = max(0, value)
            self.hopeChanged.emit()
    
    # Fear property
    @Property(int, notify=fearChanged)
    def fear(self):
        return self._fear
    
    @fear.setter
    def fear(self, value):
        if self._fear != value:
            self._fear = max(0, value)
            self.fearChanged.emit()
    
    # Ability getters/setters
    def getAbility(self, ability_name):
        return self._abilities.get(ability_name, 0)
    
    def setAbility(self, ability_name, value):
        if ability_name in self._abilities:
            self._abilities[ability_name] = value
            self.abilitiesChanged.emit()
    
    # Utility methods
    def modifyHp(self, amount):
        """Modify current HP by amount"""
        self.hpCurrent = self._hp_current + amount
    
    def modifyHope(self, amount):
        """Modify hope by amount"""
        self.hope = self._hope + amount
    
    def modifyFear(self, amount):
        """Modify fear by amount"""
        self.fear = self._fear + amount
    
    def getThreshold(self, threshold_type):
        """Get threshold value"""
        return self._thresholds.get(threshold_type, 0)
    
    def resetCharacter(self):
        """Reset character to default values"""
        self.name = "Mi Personaje"
        self.className = "Guerrero"
        self.level = 1
        self.hpCurrent = 30
        self.hpMax = 30
        self.armor = 2
        self.hope = 1
        self.fear = 0
        
        # Reset abilities
        default_abilities = {
            "Fuerza": 2,
            "Destreza": 1,
            "Carisma": 0,
            "Constitución": 1,
            "Sabiduría": 0,
            "Inteligencia": -1
        }
        for ability, value in default_abilities.items():
            self.setAbility(ability, value)
