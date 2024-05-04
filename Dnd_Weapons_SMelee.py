#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import Dnd_Weapons as  weap
from Dnd_Dice import Dice

################################################################################
#       WEAPONS -- SIMPLE MELEE
################################################################################
class Simple_Melee(weap.Weapons):
    
    def __init__(self):
        self.description = ""
        self.cost = {"cp": 100, "sp": 100, "gp": 100}
        self.weight = 100
        self.dmg_type = ""
        self.dmg_roll = [0]
        self.rarity = ""
        self.properties = []

class Club(Simple_Melee):
    
    def __init__(self):
        self.description = "Club"
        self.cost = {"cp": 0, "sp": 1, "gp": 0}
        self.weight = 2
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D4_Roll]
        self.rarity = "common"
        self.properties = ['light']
        
class Dagger(Simple_Melee):
    
    def __init__(self):
        self.description = "Dagger"
        self.cost = {"cp": 0, "sp": 0, "gp": 2}
        self.weight = 1
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D4_Roll]
        self.rarity = "common"
        self.properties = ['finesse', 'light', 'thrown']
        self.range = [20,60]

class GreatClub(Simple_Melee):
    
    def __init__(self):
        self.description = "GreatClub"
        self.cost = {"cp": 0, "sp": 2, "gp": 0}
        self.weight = 10
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = ['two_hand']

class HandAxe(Simple_Melee):
    
    def __init__(self):
        self.description = "HandAxe"
        self.cost = {"cp": 0, "sp": 0, "gp": 5}
        self.weight = 2
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['light', 'thrown']
        self.range = [20,60]
        
class Javelin(Simple_Melee):
    
    def __init__(self):
        self.description = "Javelin"
        self.cost = {"cp": 0, "sp": 5, "gp": 0}
        self.weight = 2
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['thrown']
        self.range = [30,120]
        
class LightHammer(Simple_Melee):
    
    def __init__(self):
        self.description = "LightHammer"
        self.cost = {"cp": 0, "sp": 0, "gp": 2}
        self.weight = 2
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D4_Roll]
        self.rarity = "common"
        self.properties = ['light', 'thrown']
        self.range = [20,60]

class Mace(Simple_Melee):
    
    def __init__(self):
        self.description = "Mace"
        self.cost = {"cp": 0, "sp": 0, "gp": 5}
        self.weight = 4
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = []

class Quaterstaff(Simple_Melee):
    
    def __init__(self):
        self.description = "Quaterstaff"
        self.cost = {"cp": 0, "sp": 2, "gp": 0}
        self.weight = 4
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['versatile']

class Sickle(Simple_Melee):
    
    def __init__(self):
        self.description = "Sickle"
        self.cost = {"cp": 0, "sp": 0, "gp": 1}
        self.weight = 2
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D4_Roll]
        self.rarity = "common"
        self.properties = ['light']

class Spear(Simple_Melee):
    
    def __init__(self):
        self.description = "Spear"
        self.cost = {"cp": 0, "sp": 0, "gp": 1}
        self.weight = 3
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['versatile', 'thrown']
        self.range = [20,60]