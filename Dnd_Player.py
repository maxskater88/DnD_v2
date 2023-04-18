#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import random as             rnd
import Dnd_Classes as        disp
import Dnd_Races as          rces
import Dnd_Weapons as        weap
import Dnd_Weapons_SMelee as SM
import Dnd_Weapons_SRange as SR
import Dnd_Weapons_MMelee as MM
import Dnd_Weapons_MRange as MR

################################################################################
#
#       Notes
#
################################################################################
'''
Structure:

'''
################################################################################
#       Create Player's Character
################################################################################
class player:
    num_of_players = 0
    size = 1
    races = {"Dwarf":    ["Hill Dwarf",         "Mountain Dwarf"], 
             "Elf":      ["High Elf",           "Wood Elf"],
             "Halfling": ["Lightfoot Halfling", "Stout Halfling"],
             "Human":    ["Human"]}  
    
    FightClasses = ["Barbarian",   "Bard",       "Cleric",     "Druid", 
                    "Fighter",     "Monk",       "Paladin",    "Ranger", 
                    "Rogue",       "Sorcerer",   "Warlock",    "Wizard"]
    
    stats = (       "Strength",      "Dexterity",        "Charisma",
                    "Wisdom",        "Intelligence",     "Constitution")
    
    M_Stat = {       "Strength": 0,  "Dexterity":    0,   "Charisma":     0, 
                     "Wisdom":   0,  "Intelligence": 0,   "Constitution": 0, 
                     "HP":       0,  "Armor Class":  0}
    
    proficiencies = {"Strength": 0,  "Dexterity":    0,   "Charisma":     0, 
                     "Wisdom":   0,  "Intelligence": 0,   "Constitution": 0, 
                     "HP":       0,  "Armor Class":  0}
    
    all_races = []
    for subraces in races.values():
        for race in subraces:
            all_races.append(race)
    
    ###INIT###        
    def __init__(self):
        player.count_chars(self)
        print(f"--->  CREATING CHAR #{player.num_of_players}")
        
        #Get Player to Input Custom Char Selection or Randomized
        while True:
            try:
                randomize_char = input("--->Enter 1 for a randomized char\
                                       \n--->Enter 0 for a customized char\n")
                randomize_char = int(randomize_char)
                if 0 <= randomize_char <= 1:
                    break
                else:
                    print(f"{randomize_char} is not 0 or 1.")
            except ValueError:
                print(f"{randomize_char} is not an integer.")
        
        self.base_stats =   player.M_Stat
        self.all_races = player.all_races
        if randomize_char:
            #Randomize
            pass
        else:
            #Customize
            race = player.get_race(self.all_races)
            discipline = player.get_class(self.FightClasses)
            starting_weps = player.get_starting_equip(discipline)
            self.race = race
            self.discipline = discipline
            self.starting_weps = starting_weps

            while True:
                #Get Player to Rand (let game roll 4xD6) stats or set their own stat values
                try:
                    randomize_stats = input("---> Enter 1 for random stats\
                                            \n---> Enter 0 to set stats\n")
                    randomize_stats = int(randomize_stats)
                    if 0 <= randomize_stats <= 1:
                        break
                    else:
                        print(f"{randomize_stats} is not 0 or 1.")
                except ValueError:
                    print(f"{randomize_stats} is not an integer.")
            if randomize_stats:
                #Randomize
                self.base_stats = player.roll_main_stats_rand(self.base_stats)
            else:
                #Enter Stats by Hand
                #Currently just requiring a value between min/max possible roll
                for stat in player.stats:
                    while True:
                        try:
                            self.base_stats[stat] = input(f"Enter {stat}: ")
                            self.base_stats[stat] = int(self.base_stats[stat])
                            if 3 <= self.base_stats[stat] <= 18:
                                break
                            else:
                                print(f"{self.base_stats[stat]} is not between 3 and 18.")
                        except ValueError:
                            print(f"{self.base_stats[stat]} is not an integer.")
                         
    def get_race(all_races):
        #Could add exception to load previous char 
        selected_race = None
        Race = None
        #have user select race/sub-race
        print("LETS BUILD A CHARACTER TO PLAY IN OUR D&D GAME!")
        while selected_race not in(all_races):
            selected_race = input(f"Select a Race:\n {all_races} \n")
        #assign the Race to a Class Object based on what was entered
        if selected_race == "Lightfoot Halfling":
            Race = rces.Lightfoot_Halfling()
        elif selected_race == "Stout Halfling":
            Race = rces.Stout_Halfling()
        elif selected_race == "High Elf":
            Race = rces.High_Elf()
        elif selected_race == "Wood Elf":
            Race = rces.Wood_Elf()
        elif selected_race == "Hill Dwarf":
            Race = rces.Hill_Dwarf()
        elif selected_race == "Mountain Dwarf":
            Race = rces.Mountain_Dwarf()
        else:
            print("ERROR E0001")
        return Race

    def get_class(FightClasses):
        selected_class = ""
        print("LETS CHOOSE A CLASS FOR OUR CHARACTER!")
        while selected_class not in(FightClasses):
            selected_class = input(f"Select a Class:\n {FightClasses} \n")
        #Assigning Class of Warrior to a Class Object based on what was entered 
        if   selected_class == "Barbarian":
            selected_class = disp.Barbarian()
        elif selected_class == "Bard":
            selected_class = disp.Bard()
        elif selected_class == "Cleric":
            selected_class = disp.Cleric()
        elif selected_class == "Druid":
            selected_class = disp.Druid()
        elif selected_class == "Fighter":
            selected_class = disp.Fighter()
        elif selected_class == "Monk":
            selected_class = disp.Monk()
        elif selected_class == "Paladin":
            selected_class = disp.Paladin()
        elif selected_class == "Ranger":
            selected_class = disp.Ranger()  
        elif selected_class == "Rogue":
            selected_class = disp.Rogue()
        elif selected_class == "Sorcerer":
            selected_class = disp.Sorcerer()
        elif selected_class == "Warlock":
            selected_class = disp.Warlock()
        elif selected_class == "Wizard":
            selected_class = disp.Wizard()
        else:
            print("ERROR E0002")
        return selected_class    

    def get_starting_equip(discipline):
        if isinstance(discipline, disp.Barbarian):
            #Greataxe OR any martial mele
            #2 HandAxe OR any simple weapon
            #explorer's pack and 4 javelins
            wep_sel = ""
            inital = None
            while wep_sel not in("1a", "1b", "2a", "2b", "3"):
                wep_sel = input(
                    f'''Choose one of the following Starting Weapon(s) (enter 1a, 1b, 2a, 2b, or 3):\n
                    (1)(a) 1 GreatAxe, or (1)(b) any 1 of: {weap.Weapons.martial_melee}\n
                    (2)(a) 2 HandAxe   or (2)(b) any 1 of: {weap.Weapons.simple_melee} {weap.Weapons.simple_range}\n
                    (3) 1 Explorer's Pack and 4 Javelins\n''')
            if wep_sel == "1a":
                inital = [MM.GreatAxe]
            elif wep_sel == "1b":
                inital = input("Enter the Wepon you want")
                #Convert this to a class? Is this A LOT of Elifs?
                #globals()[class_name]
            elif wep_sel == "2a":
                pass
            elif wep_sel == "2b":
                pass
            elif wep_sel == "3":
                pass
            else:
                print("ERROR E0003")



    def D4_Roll():
        return rnd.randint(1,4)
    def D6_Roll():
        return rnd.randint(1,6)
    def D8_Roll():
        return rnd.randint(1,8)
    def D10_Roll():
        return rnd.randint(1,10)
    def D12_Roll():
        return rnd.randint(1,12)  
    
    def count_chars(self):
        player.num_of_players += 1
    
    def roll_main_stats_rand(Main_Stat):
        '''
        Roll random initial stats. 
        Roll 4 x 6-sided die and sum the top 3 values for each stat (not HP)
        '''
        for stat in player.stats:
            sumTot_orig = []
            sumTot_ord = []
            for i in range(4):
                sumTot_orig.append(player.D6_Roll())
            sumTot_ord = list(sumTot_orig)
            sumTot_ord.sort(reverse=True)
            sol = sum(sumTot_ord[0:3])
            print(f"For {stat} your d6 roll(s) are: {sumTot_orig} and your total is {sol}")
            Main_Stat[stat] += sol
        return Main_Stat
    

            
