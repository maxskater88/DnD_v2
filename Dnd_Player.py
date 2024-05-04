#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import random as rnd
import copy
import Dnd_Classes
import Dnd_Weapons as Weap
import Dnd_Weapons_SMelee as SM
import Dnd_Weapons_SRange as SR
import Dnd_Weapons_MMelee as MM
import Dnd_Weapons_MRange as MR
from Dnd_Classes import Discipline as Disp
from Dnd_Races import Race as Rces
from Dnd_Dice import Dice
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
class Player:
    num_of_players = 0
    size = 1
    
    stats = (       "Strength",      "Dexterity",        "Charisma",
                    "Wisdom",        "Intelligence",     "Constitution")
    
    stats_additional = ("HP", "Armor Class")
    
    M_Stat = {       "Strength": 0,  "Dexterity":    0,   "Charisma":     0, 
                     "Wisdom":   0,  "Intelligence": 0,   "Constitution": 0, 
                     "HP":       0,  "Armor Class":  0}
    
    proficiencies = {"Strength": 0,  "Dexterity":    0,   "Charisma":     0, 
                     "Wisdom":   0,  "Intelligence": 0,   "Constitution": 0, 
                     "HP":       0,  "Armor Class":  0}
  
    ### INIT ###        
    def __init__(self):
        Player.count_chars(self)
        self.base_stats = copy.copy(Player.M_Stat)
        self.all_races = copy.copy(Rces.all_races)
        self.fighting_classes = copy.copy(Disp.fighting_classes)
        self.level = 0
        
        print(f"--->  CREATING CHAR #{Player.num_of_players}")
        randomize_char = Player.build_custom_or_rand()
        
        # Get Primary Character info (race, class, starting equipment)
        # Note: Could create a binary and a list user input method so that I dont have to code that out every time
        self.race = Rces._initial_race(self.all_races, randomize_char)
        self.discipline = Disp._initial_class(self.fighting_classes, randomize_char)
        Player._initial_stats(self, randomize_char)
        # self.starting_weps = starting_weps
        self.testing = True


    def count_chars(self):
        Player.num_of_players += 1
        

    def build_custom_or_rand():
        #Get Player to Input Custom Char Selection or Randomized
        randomize_char = Player.check_input("::Enter 0 for a customized char\n::Enter 1 for a randomized char\n", 0, 1)
        return randomize_char     


    def _initial_stats(self, randomize):
        if randomize:
            Player._main_stats_rand_roll(self)
        else:
            points_cost = {8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9}
            max_cost = 27
            print(f"For each stat you must select a value from the list:\n{points_cost}\nAnd the total of that stats' cost must be at most: {max_cost}")
            #There is a better way to do this loop...
            while True:
                current_cost = 0
                for stat in Player.stats:
                    stat_cur = Player.check_input(f"Select a value for {stat}:\n", 8, 15)
                    current_cost += points_cost[stat_cur]
                    self.base_stats[stat] = stat_cur
                if current_cost <= max_cost:
                    break
                else:
                    print(f"You choose too many stats: {self.base_stats}.\nYour total was {current_cost} out of {max_cost}")


    def _main_stats_rand_roll(self):
        '''
        Roll random initial stats. 
        Roll 4 x 6-sided die and sum the top 3 values for each stat
        '''
        for stat in Player.stats:
            sumTot = []
            for _ in range(4):
                sumTot.append(Dice.D6_Roll())
            sumTot = sorted(list(sumTot), reverse=True)
            sol = sum(sumTot[0:3])
            print(f"For {stat} your d6 roll(s) are: {sumTot} and your total is {sol}")
            self.base_stats[stat] = sol


    def check_input(text, a, b):
        while True:
            try:
                player_input = int(input(text))
                if a <= player_input <= b:
                    break
                else:
                    print(f"Integer not within range of [{a}, {b}]")
            except ValueError:
                print("Please enter a number")   
        return player_input

  
    def _get_starting_equip(discipline, randomize):        
        if isinstance(discipline, Dnd_Classes.Barbarian):
            #Greataxe OR any martial mele
            #2 HandAxe OR any simple weapon
            #explorer's pack and 4 javelins
            wep_sel = ""
            inital = None
            selections = ["1a", "1b", "2a", "2b", "3"]
            if randomize:
                wep_sel = selections[rnd.randrange(len(selections))]
            while wep_sel not in selections:
                wep_sel = input(
                    f'''Choose one of the following Starting Weapon(s) (enter 1a, 1b, 2a, 2b, or 3):\n
                    (1)(a) 1 GreatAxe, or (1)(b) any 1 of: {Weap.Weapons.martial_melee}\n
                    (2)(a) 2 HandAxe   or (2)(b) any 1 of: {Weap.Weapons.simple_melee} {Weap.Weapons.simple_range}\n
                    (3) 1 Explorer's Pack and 4 Javelins\n''')
            if wep_sel == "1a":
                inital = [MM.GreatAxe]
            elif wep_sel == "1b":
                inital = input("Enter the Wepon you want")
                #Convert this to a class? Is this A LOT of Elifs? maybe a check in list of strings, then an eval func?
                #globals()[class_name]
            elif wep_sel == "2a":
                pass
            elif wep_sel == "2b":
                pass
            elif wep_sel == "3":
                pass
            else:
                print("ERROR E0003")