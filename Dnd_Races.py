#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
# import Dnd_Player as  pler
# import Dnd_Weapons as weap 
# import Dnd_Races as   rces

################################################################################
#       RACES
################################################################################
class Race:
    race_mod = {"Strength": 0,  "Dexterity":    0,   "Charisma":     0, 
                "Wisdom":   0,  "Intelligence": 0,   "Constitution": 0, 
                "HP":       0,  "Armor Class":  0}
    
    languages = ["Common", "Dwarvish", "Elvish", "Halfling"]
    
    def __init__(self):
        self.abilities_names = []
        self.description = '''ENTER RACE INFO'''
        self.speed = 25
        self.size = "medium"
    
class Hill_Dwarf(Race):
    race_mod = {"Strength": 0,  "Dexterity":    0,   "Charisma":     0, 
                "Wisdom":   1,  "Intelligence": 0,   "Constitution": 2, 
                "HP":       1,  "Armor Class":  0}
    def __init__(self):
        #super().__init__(Main_Stat) 
        self.abilities_names = []
        self.description = '''Its  a Hill Dwarf Bro.'''
        self.speed = 25
        self.size = "medium"
        self.languages = ["Common", "Dwarvish"]
 
class Mountain_Dwarf(Race):
    race_mod = {"Strength": 2,  "Dexterity":    0,   "Charisma":     0, 
                "Wisdom":   0,  "Intelligence": 0,   "Constitution": 2, 
                "HP":       0,  "Armor Class":  0}
    def __init__(self):
        #super().__init__(Main_Stat) 
        self.abilities_names = []     
        self.description = '''Its  a Mtn Dwarf Bro.'''   
        self.speed = 25
        self.size = "medium"
        self.languages = ["Common", "Dwarvish"]
    
class High_Elf(Race):
    race_mod = {"Strength": 0,  "Dexterity":    2,   "Charisma":     0, 
                "Wisdom":   0,  "Intelligence": 1,   "Constitution": 0, 
                "HP":       0,  "Armor Class":  0}
    def __init__(self):
        #super().__init__(Main_Stat) 
        self.abilities_names = []
        self.description = '''Its  a High Elf Bro.'''
        self.speed = 30
        self.size = "medium"
        self.languages = ["Common", "Elvish"]
 
class Wood_Elf(Race):
    race_mod = {"Strength": 0,  "Dexterity":    2,   "Charisma":     0, 
                "Wisdom":   1,  "Intelligence": 0,   "Constitution": 0, 
                "HP":       0,  "Armor Class":  0}
    def __init__(self):
        #super().__init__(Main_Stat) 
        self.abilities_names = []     
        self.description = '''Its  a Wood Elf Bro.'''   
        self.speed = 35
        self.size = "medium"
        self.languages = ["Common", "Elvish"]
    
class Lightfoot_Halfling(Race):
    race_mod = {"Strength": 0,  "Dexterity":    2,   "Charisma":     1, 
                "Wisdom":   0,  "Intelligence": 0,   "Constitution": 0, 
                "HP":       0,  "Armor Class":  0}
    def __init__(self):
        #super().__init__(Main_Stat) 
        self.abilities_names = []     
        self.description = '''Its  a Lightfoot Halfling Bro.'''     
        self.speed = 25
        self.size = "small"  
        self.languages = ["Common", "Halfling"] 

class Stout_Halfling(Race):
    race_mod = {"Strength": 0,  "Dexterity":    2,   "Charisma":     0, 
                "Wisdom":   0,  "Intelligence": 0,   "Constitution": 1, 
                "HP":       0,  "Armor Class":  0}
    def __init__(self):
        #super().__init__(Main_Stat) 
        self.abilities_names = []     
        self.description = '''Its  a Stout Halfling Bro.'''    
        self.speed = 25
        self.size = "small"   
        self.languages = ["Common", "Halfling"]
   
class Human(Race):
    race_mod = {"Strength": 1,  "Dexterity":    1,   "Charisma":     1, 
                "Wisdom":   1,  "Intelligence": 1,   "Constitution": 1, 
                "HP":       1,  "Armor Class":  0}
    def __init__(self):
        #super().__init__(Main_Stat) 
        self.abilities_names = []     
        self.description = '''Its  a Human Bro.'''  
        self.speed = 30
        self.size = "medium"    
        self.languages = ["Common"]
        
