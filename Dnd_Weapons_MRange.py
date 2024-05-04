#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import Dnd_Weapons as  weap
from Dnd_Dice import Dice

################################################################################
#       WEAPONS -- MARTIAL RANGE
################################################################################
class Martial_Range(weap.Weapons):
    
    def __init__(self):
        self.description = ""
        self.cost = {"cp": 100, "sp": 100, "gp": 100}
        self.weight = 100
        self.dmg_type = ""
        self.dmg_roll = [0]
        self.rarity = ""
        self.properties = []

class Blowgun(Martial_Range):
    
    def __init__(self):
        self.description = "Blowgun"
        self.cost = {"cp": 0, "sp": 0, "gp": 10}
        self.weight = 1
        self.dmg_type = "piercing"
        self.dmg_roll = [1]
        self.rarity = "common"
        self.properties = ['ammunition', 'loading']
        self.range = [25,100]
        
class HandCrosbow(Martial_Range):
    
    def __init__(self):
        self.description = "HandCrosbow"
        self.cost = {"cp": 0, "sp": 0, "gp": 75}
        self.weight = 3
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['ammunition', 'light', 'loading']
        self.range = [30,120]
        
class HeavyCrossbow(Martial_Range):
    
    def __init__(self):
        self.description = "HeavyCrossbow"
        self.cost = {"cp": 0, "sp": 0, "gp": 50}
        self.weight = 18
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D10_Roll]
        self.rarity = "common"
        self.properties = ['ammunition', 'heavy', 'loading']
        self.range = [100,400]
        
class Longbow(Martial_Range):
    
    def __init__(self):
        self.description = "Longbow"
        self.cost = {"cp": 0, "sp": 0, "gp": 50}
        self.weight = 2
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = ['ammunition', 'heavy', 'two_hand']
        self.range = [150,600]

class Net(Martial_Range):
    
    def __init__(self):
        self.description = "Net"
        self.cost = {"cp": 0, "sp": 0, "gp": 1}
        self.weight = 3
        self.dmg_type = ""
        self.dmg_roll = [0]
        self.rarity = "common"
        self.properties = ['special', 'thrown']
        self.range = [5,15]
        
