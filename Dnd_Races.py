#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import random as rnd
# import Dnd_Player as  pler
# import Dnd_Weapons as weap 
# import Dnd_Races as   rces

################################################################################
#       RACES
################################################################################
class Race:
    
    races = {"Dwarf":    ["Hill Dwarf",         "Mountain Dwarf"], 
             "Elf":      ["High Elf",           "Wood Elf"],
             "Halfling": ["Lightfoot Halfling", "Stout Halfling"],
             "Human":    ["Human"]}  
    
    all_races = []
    for subraces in races.values():
        for race in subraces:
            all_races.append(race)
    
    race_mod = {"Strength": 0,  "Dexterity":    0,   "Charisma":     0, 
                "Wisdom":   0,  "Intelligence": 0,   "Constitution": 0, 
                "HP":       0,  "Armor Class":  0}
    
    languages = ["Common", "Dwarvish", "Elvish", "Halfling"]
    
    def __init__(self):
        self.abilities_names = []
        self.description = '''ENTER RACE INFO'''
        self.speed = 25
        self.size = "medium"
    
    def _initial_race(all_races, randomize):
        #Could add exception to load previous char 
        print("LETS BUILD A CHARACTER TO PLAY IN OUR D&D GAME!")
        selected_race = None
        if randomize:
            rnd_int = rnd.randrange(len(all_races))
            print(f"Your randomly selected race is: {all_races[rnd_int]}")
            return Race.get_race_obj(all_races[rnd_int])   
        
        while selected_race not in(all_races):
            selected_race = input(f"Select a Race:\n {all_races} \n")
        return Race.get_race_obj(selected_race)
    
    def get_race_obj(selected_race):
        #helper funct to get race obj back
        if selected_race == "Lightfoot Halfling":
            Race = Lightfoot_Halfling()
        elif selected_race == "Stout Halfling":
            Race = Stout_Halfling()
        elif selected_race == "High Elf":
            Race = High_Elf()
        elif selected_race == "Wood Elf":
            Race = Wood_Elf()
        elif selected_race == "Hill Dwarf":
            Race = Hill_Dwarf()
        elif selected_race == "Mountain Dwarf":
            Race = Mountain_Dwarf()
        elif selected_race == "Human":
            Race = Human()
        else:
            print("ERROR E0001")
        return Race
    
    
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
        
