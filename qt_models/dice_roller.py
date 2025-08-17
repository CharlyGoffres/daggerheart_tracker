"""
Dice Roller Model for Qt/QML Version
Handles all dice rolling mechanics with animations and results
"""

import random
from PySide6.QtCore import QObject, Signal, Slot, Property, QTimer

class DiceRoller(QObject):
    """Dice rolling system with Qt integration"""
    
    # Signals
    rollStarted = Signal()
    rollFinished = Signal(list, int, str)  # dice_results, total, result_type
    diceAnimationFrame = Signal(list)  # animated dice values
    
    def __init__(self):
        super().__init__()
        self._is_rolling = False
        self._animation_timer = QTimer()
        self._animation_timer.timeout.connect(self._animate_dice)
        self._animation_frames = 0
        self._max_animation_frames = 15
        self._final_result = None
    
    @Property(bool, notify=rollStarted)
    def isRolling(self):
        return self._is_rolling
    
    @Slot(str, int, str)
    def rollAbility(self, roll_type, modifier, ability_name):
        """Roll for an ability check"""
        if self._is_rolling:
            return
        
        self._is_rolling = True
        self.rollStarted.emit()
        
        # Calculate dice based on roll type
        dice_results = self._calculate_dice_roll(roll_type)
        
        # Calculate total
        total = sum(dice_results) + modifier
        
        # Determine result type
        result_type = self._determine_result_type(total)
        
        # Store final result for animation
        self._final_result = (dice_results, total, result_type, ability_name, modifier)
        
        # Start animation
        self._animation_frames = 0
        self._animation_timer.start(80)  # 80ms per frame
    
    @Slot(str, int)
    def rollDamage(self, die_type, modifier):
        """Roll damage dice"""
        if self._is_rolling:
            return
        
        # Extract die size (e.g., "d6" -> 6)
        die_size = int(die_type.replace('d', ''))
        
        # Roll the die
        roll = random.randint(1, die_size)
        total = roll + modifier
        
        # Emit immediate result for damage
        self.rollFinished.emit([roll], total, "damage")
    
    @Slot(int, int)
    def rollCustomDice(self, num_dice, die_size):
        """Roll custom dice"""
        if self._is_rolling:
            return
        
        results = []
        for _ in range(num_dice):
            results.append(random.randint(1, die_size))
        
        total = sum(results)
        self.rollFinished.emit(results, total, "custom")
    
    def _calculate_dice_roll(self, roll_type):
        """Calculate dice results based on roll type"""
        if roll_type == "Normal":
            return [random.randint(1, 12), random.randint(1, 12)]
        elif roll_type == "Ventaja":
            rolls = [random.randint(1, 12) for _ in range(3)]
            return sorted(rolls, reverse=True)[:2]
        elif roll_type == "Desventaja":
            rolls = [random.randint(1, 12) for _ in range(3)]
            return sorted(rolls)[:2]
        elif roll_type == "Doble Ventaja":
            rolls = [random.randint(1, 12) for _ in range(4)]
            return sorted(rolls, reverse=True)[:2]
        elif roll_type == "Triple Ventaja":
            rolls = [random.randint(1, 12) for _ in range(5)]
            return sorted(rolls, reverse=True)[:2]
        else:
            return [random.randint(1, 12), random.randint(1, 12)]
    
    def _determine_result_type(self, total):
        """Determine the type of result based on total"""
        if total >= 22:
            return "critical_success"
        elif total >= 16:
            return "major_success"
        elif total >= 10:
            return "minor_success"
        else:
            return "failure"
    
    def _animate_dice(self):
        """Animation frame for dice rolling"""
        if self._animation_frames < self._max_animation_frames:
            # Generate random dice for animation
            animated_dice = [random.randint(1, 12), random.randint(1, 12)]
            self.diceAnimationFrame.emit(animated_dice)
            self._animation_frames += 1
        else:
            # Finish animation
            self._animation_timer.stop()
            self._is_rolling = False
            
            # Emit final result
            dice_results, total, result_type, ability_name, modifier = self._final_result
            self.rollFinished.emit(dice_results, total, result_type)
    
    @Slot()
    def stopRoll(self):
        """Stop current roll animation"""
        if self._is_rolling:
            self._animation_timer.stop()
            self._is_rolling = False
