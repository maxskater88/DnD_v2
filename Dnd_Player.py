#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import random as             rnd
import Dnd_Classes as        discipline
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
    
    stats_additional = ("HP", "Armor Class")
    
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
  
  
    ### INIT ###        
    def __init__(self):
        player.count_chars(self)
        self.base_stats =   player.M_Stat
        self.all_races = player.all_races
        self.level = 0
        
        print(f"--->  CREATING CHAR #{player.num_of_players}")
        randomize_char = player.build_custom_or_rand()
        
        # Get Primary Character info (race, class, starting equipment)
        # Note: Could create a binary and a list user input method so that I dont have to code that out every time
        self.race = player.get_race(self.all_races, randomize_char)
        self.discipline = player.get_class(self.FightClasses, randomize_char)
        player.initial_stats(self, randomize_char)
        # self.starting_weps = starting_weps


    def build_custom_or_rand():
        #Get Player to Input Custom Char Selection or Randomized
        randomize_char = player.check_input("::Enter 0 for a customized char\n::Enter 1 for a randomized char\n", 0, 1)
        return randomize_char     
 
                         
    def get_race(all_races, randomize):
        #Could add exception to load previous char 
        print("LETS BUILD A CHARACTER TO PLAY IN OUR D&D GAME!")
        selected_race = None
        if randomize:
            rnd_num = rnd.randrange(len(all_races))
            print(f"Your randomly select race is: {all_races[rnd_num]}")
            return player.get_race_obj(all_races[rnd_num])   
        
        while selected_race not in(all_races):
            selected_race = input(f"Select a Race:\n {all_races} \n")
        return player.get_race_obj(selected_race)


    def get_class(FightClasses, randomize):
        print("LETS CHOOSE A CLASS FOR OUR CHARACTER!")
        selected_class = ""
        if randomize:
            rnd_num = rnd.randrange(len(FightClasses))
            print(f"Your randomly selected class is: {FightClasses[rnd_num]}")
            return player.get_class_obj(FightClasses[rnd_num])
    
        while selected_class not in(FightClasses):
            selected_class = input(f"Select a Class:\n {FightClasses} \n")
        return player.get_class_obj(selected_class)


    def initial_stats(self, randomize):
        if randomize:
            self.base_stats = player.main_stats_rand_roll()
        else:
            points_cost = {8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9}
            max_cost = 27
            print(f"For each stat you must select a value from the list:\n{points_cost}\nAnd the total of that stats' cost must be at most: {max_cost}")
            while True:
                current_cost = 0
                for stat in player.stats:
                    stat_cur = player.check_input(f"Select a value for {stat}:\n", 8, 15)
                    current_cost += points_cost[stat_cur]
                    self.base_stats[stat] = stat_cur
                if current_cost <= max_cost:
                    break


    def main_stats_rand_roll(self):
        '''
        Roll random initial stats. 
        Roll 4 x 6-sided die and sum the top 3 values for each stat
        '''
        for stat in player.stats:
            sumTot_orig = []
            sumTot_ord = []
            for i in range(4):
                sumTot_orig.append(player.D6_Roll())
            sumTot_ord = list(sumTot_orig).sort(reverse=True)
            # sumTot_ord.sort(reverse=True)
            sol = sum(sumTot_ord[0:3])
            print(f"For {stat} your d6 roll(s) are: {sumTot_orig} and your total is {sol}")
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
    def D20_Roll():
        return rnd.randint(1,20) 
    
    
    def count_chars(self):
        player.num_of_players += 1
    
      
    def get_race_obj(selected_race):
        #helper funct to get race obj back
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
        elif selected_race == "Human":
            Race = rces.Human()
        else:
            print("ERROR E0001")
        return Race

    
    def get_class_obj(selected_class):
        #helper funct to get class obj back
        if   selected_class == "Barbarian":
            selected_class = discipline.Barbarian()
        elif selected_class == "Bard":
            selected_class = discipline.Bard()
        elif selected_class == "Cleric":
            selected_class = discipline.Cleric()
        elif selected_class == "Druid":
            selected_class = discipline.Druid()
        elif selected_class == "Fighter":
            selected_class = discipline.Fighter()
        elif selected_class == "Monk":
            selected_class = discipline.Monk()
        elif selected_class == "Paladin":
            selected_class = discipline.Paladin()
        elif selected_class == "Ranger":
            selected_class = discipline.Ranger()  
        elif selected_class == "Rogue":
            selected_class = discipline.Rogue()
        elif selected_class == "Sorcerer":
            selected_class = discipline.Sorcerer()
        elif selected_class == "Warlock":
            selected_class = discipline.Warlock()
        elif selected_class == "Wizard":
            selected_class = discipline.Wizard()
        else:
            print("ERROR E0002")
        return selected_class    


    def get_starting_equip(discipline, randomize):
        if isinstance(discipline, discipline.Barbarian):
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