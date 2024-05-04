#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import Dnd_Weapons as  weap
from Dnd_Dice import Dice
################################################################################
#       WEAPONS -- MARTIAL MELEE
################################################################################
class Martial_Melee(weap.Weapons):
    
    def __init__(self):
        self.description = ""
        self.cost = {"cp": 100, "sp": 100, "gp": 100}
        self.weight = 100
        self.dmg_type = ""
        self.dmg_roll = [0]
        self.rarity = ""
        self.properties = []

class BattleAxe(Martial_Melee):
    
    def __init__(self):
        self.description = "BattleAxe"
        self.cost = {"cp": 0, "sp": 0, "gp": 10}
        self.weight = 4
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = ['versatile']
        
class Flail(Martial_Melee):
    
    def __init__(self):
        self.description = "Flail"
        self.cost = {"cp": 0, "sp": 0, "gp": 10}
        self.weight = 2
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = []
        
class Glaive(Martial_Melee):
    
    def __init__(self):
        self.description = "Glaive"
        self.cost = {"cp": 0, "sp": 0, "gp": 20}
        self.weight = 6
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D10_Roll]
        self.rarity = "common"
        self.properties = ['heavy', 'reach', 'two_hand']
        
class GreatAxe(Martial_Melee):
    
    def __init__(self):
        self.description = "GreatAxe"
        self.cost = {"cp": 0, "sp": 0, "gp": 30}
        self.weight = 7
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D12_Roll]
        self.rarity = "common"
        self.properties = ['heavy', 'two_hand']

class GreatSword(Martial_Melee):
    
    def __init__(self):
        self.description = "GreatSword"
        self.cost = {"cp": 0, "sp": 0, "gp": 50}
        self.weight = 6
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D6_Roll, Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['heavy', 'two_hand']
        
class Halberd(Martial_Melee):
    
    def __init__(self):
        self.description = "Halberd"
        self.cost = {"cp": 0, "sp": 0, "gp": 20}
        self.weight = 6
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D10_Roll]
        self.rarity = "common"
        self.properties = ['heavy', 'reach', 'two_hand']
        
class Lance(Martial_Melee):
    
    def __init__(self):
        self.description = "Lance"
        self.cost = {"cp": 0, "sp": 0, "gp": 10}
        self.weight = 6
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D12_Roll]
        self.rarity = "common"
        self.properties = ['special', 'reach']
        
class Longsword(Martial_Melee):
    
    def __init__(self):
        self.description = "Longsword"
        self.cost = {"cp": 0, "sp": 0, "gp": 15}
        self.weight = 3
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = ['versatile']

class Maul(Martial_Melee):
    
    def __init__(self):
        self.description = "Maul"
        self.cost = {"cp": 0, "sp": 0, "gp": 10}
        self.weight = 10
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D6_Roll, Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['heavy', 'two_hand']
        
class Morningstar(Martial_Melee):
    
    def __init__(self):
        self.description = "Morningstar"
        self.cost = {"cp": 0, "sp": 0, "gp": 15}
        self.weight = 4
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = []
        
class Pike(Martial_Melee):
    
    def __init__(self):
        self.description = "Pike"
        self.cost = {"cp": 0, "sp": 0, "gp": 5}
        self.weight = 18
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D10_Roll]
        self.rarity = "common"
        self.properties = ['heavy', 'reach', 'two_hand']
        
class Rapier(Martial_Melee):
    
    def __init__(self):
        self.description = "Rapier"
        self.cost = {"cp": 0, "sp": 0, "gp": 25}
        self.weight = 2
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = ['finesse']

class Scimitar(Martial_Melee):
    
    def __init__(self):
        self.description = "Scimitar"
        self.cost = {"cp": 0, "sp": 0, "gp": 25}
        self.weight = 3
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['finesse', 'light']
        
class Shortsword(Martial_Melee):
    
    def __init__(self):
        self.description = "Shortsword"
        self.cost = {"cp": 0, "sp": 0, "gp": 10}
        self.weight = 2
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['finesse', 'light']
        
class Trident(Martial_Melee):
    
    def __init__(self):
        self.description = "Trident"
        self.cost = {"cp": 0, "sp": 0, "gp": 5}
        self.weight = 4
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D6_Roll]
        self.rarity = "common"
        self.properties = ['versatile', 'thrown']
        self.range = [20,60]
        
class Warpick(Martial_Melee):
    
    def __init__(self):
        self.description = "Warpick"
        self.cost = {"cp": 0, "sp": 0, "gp": 5}
        self.weight = 2
        self.dmg_type = "piercing"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = []

class Warhammer(Martial_Melee):
    
    def __init__(self):
        self.description = "Warhammer"
        self.cost = {"cp": 0, "sp": 0, "gp": 15}
        self.weight = 2
        self.dmg_type = "bludgeoning"
        self.dmg_roll = [Dice.D8_Roll]
        self.rarity = "common"
        self.properties = ['versatile']
        
class Whip(Martial_Melee):
    
    def __init__(self):
        self.description = "Whip"
        self.cost = {"cp": 0, "sp": 0, "gp": 2}
        self.weight = 3
        self.dmg_type = "slashing"
        self.dmg_roll = [Dice.D4_Roll]
        self.rarity = "common"
        self.properties = ['finesse', 'reach']

