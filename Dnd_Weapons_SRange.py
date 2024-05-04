#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import Dnd_Weapons as  weap
from Dnd_Dice import Dice

################################################################################
#       WEAPONS -- SIMPLE RANGE
################################################################################
class Simple_Range(weap.Weapons):
    
    def __init__(self):
        self.description = ""
        self.cost = {"cp": 100, "sp": 100, "gp": 100}
        self.weight = 100
        self.dmg_type = ""
        self.dmg_roll = [0]
        self.rarity = ""
        self.properties = []

class LightCrossbow(Simple_Range):
    
    def __init__(self):
        self.description = "LightCrossbow"
        self.cost = {"cp": 0, "sp": 0, "gp": 25}
        self.weight = 5
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = ['ammunition', 'loading', 'two_hand']
        self.range = [80,320]
        
class Dart(Simple_Range):
    
    def __init__(self):
        self.description = "Dart"
        self.cost = {"cp": 5, "sp": 0, "gp": 0}
        self.weight = 0.25
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D4_Roll]
        self.rarity = "common"
        self.properties = ['finesse', 'thrown']
        self.range = [20,60]
        
class Shortbow(Simple_Range):
    
    def __init__(self):
        self.description = "Shortbow"
        self.cost = {"cp": 0, "sp": 0, "gp": 25}
        self.weight = 2
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['ammunition', 'two_hand']
        self.range = [80,320]
        
class Sling(Simple_Range):
    
    def __init__(self):
        self.description = "Sling"
        self.cost = {"cp": 0, "sp": 1, "gp": 0}
        self.weight = 0.01
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D4_Roll]
        self.rarity = "common"
        self.properties = ['ammunition']
        self.range = [30,120]

