#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import random as rnd
import Dnd_Player as  pler
import Dnd_Weapons as weap 
import Dnd_Weapons_SMelee as SM
import Dnd_Weapons_SRange as SR
import Dnd_Weapons_MMelee as MM
import Dnd_Weapons_MRange as MR
from Dnd_Dice import Dice

################################################################################
#       DICIPLINES (CLASSES)
################################################################################
class Discipline: 
    
    # skills = {  'Strength':['Athletics'],
    #             'Dexterity':['Acrobatics', 'Slight of Hand', 'Stealth'],
    #             'Intelligence':['Arcana','History','Investigation','Nature','Religion'],
    #             'Wisdom':['Animal Handling','Insight','Medicine','Perception','Survival'],
    #             'Charisma':['Deception','Intimidation','Performance','Persuasion']}
    
    fighting_classes = ["Barbarian",   "Bard",       "Cleric",     "Druid", 
                    "Fighter",     "Monk",       "Paladin",    "Ranger", 
                    "Rogue",       "Sorcerer",   "Warlock",    "Wizard"]
    
    def __init__(self):
        self.description = ""
        self.class_name = ""
        self.primary_ability = ()
        self.hit_die = Dice.D8_Roll()
        self.saving_throw = ()
    
    
    def _initial_class(fighting_classes, randomize):
        print("LETS CHOOSE A CLASS FOR OUR CHARACTER!")
        selected_class = ""
        if randomize:
            rnd_int = rnd.randrange(len(fighting_classes))
            print(f"Your randomly selected class is: {fighting_classes[rnd_int]}")
            return Discipline.get_class_obj(fighting_classes[rnd_int])
    
        while selected_class not in(fighting_classes):
            selected_class = input(f"Select a Class:\n {fighting_classes} \n")
        return Discipline.get_class_obj(selected_class)
        
        
    def get_class_obj(selected_class):
        #helper funct to get class obj back
        if   selected_class == "Barbarian":
            selected_class = Barbarian()
        elif selected_class == "Bard":
            selected_class = Bard()
        elif selected_class == "Cleric":
            selected_class = Cleric()
        elif selected_class == "Druid":
            selected_class = Druid()
        elif selected_class == "Fighter":
            selected_class = Fighter()
        elif selected_class == "Monk":
            selected_class = Monk()
        elif selected_class == "Paladin":
            selected_class = Paladin()
        elif selected_class == "Ranger":
            selected_class = Ranger()  
        elif selected_class == "Rogue":
            selected_class = Rogue()
        elif selected_class == "Sorcerer":
            selected_class = Sorcerer()
        elif selected_class == "Warlock":
            selected_class = Warlock()
        elif selected_class == "Wizard":
            selected_class = Wizard()
        else:
            print("ERROR E0002")
        return selected_class    
        
class Barbarian(Discipline):
    def __init__(self):
        self.description = "A fierce warrior of primitive background who can enter a battle rage"
        self.class_name = "Barbarian"
        self.primary_ability = ("Strength")
        self.hit_die = Dice.D12_Roll()
        self.saving_throw = ("Strength", "Constitution")
        self.weapon_prof = SM.Simple_Melee
        self.armor_prof = ['light armor', 'medium armor', 'shields']
        self.weaps_prof = [SM.Simple_Melee, MM.Martial_Melee]
        self.test = 1

class Bard(Discipline):
    def __init__(self):
        super().__init__() 
        #Enter stuff here
        self.description = "An inspiring magician whose power echoes the music of creation"
        self.class_name = "Bard"
        self.primary_ability = ("Charisma")
        self.saving_throw = ("Dexterity", "Charisma")
        self.armor_prof = ['light armor', 'medium armor', 'shields']
        
        
class Cleric(Discipline):
    def __init__(self):
        #Enter stuff here
        self.description = "A priestly champion who wields divine magic in service of a higher power"
        self.class_name = "Cleric"
        self.primary_ability = ("Wisdom")
        self.saving_throw = ("Wisdom", "Charisma")
         
class Druid(Discipline):
    def __init__(self):
        #Enter stuff here
        self.description = "A priest of the Old Faith, wielding the powers of nature — moonlight and plant growth, fire and lightning — and adopting animal forms"
        self.class_name = "Druid"
        self.primary_ability = ("Wisdom")
        self.saving_throw = ("Intelligence", "Wisdom")
        
class Fighter(Discipline):
    def __init__(self):
        #Enter stuff here
        
        self.description = "A master of martial combat, skilled with a variety of weapons and armor"
        self.class_name = "Fighter"
        self.primary_ability = (Fighter.select_primary_ability())
        self.hit_die = Dice.D10_Roll()
        self.saving_throw = ("Strength", "Constitution")
    
    def select_primary_ability():
        primary_ability = ""
        while primary_ability not in("Strength", "Dexterity"):
            primary_ability = input(f"Select one of either Strength or Dexterity as your main statistic\n")
        return primary_ability
    
class Monk(Discipline):
    def __init__(self):
        #Enter stuff here
        self.description = "A master of martial arts, harnessing the power of the body in pursuit of physical and spiritual perfection"
        self.class_name = "Monk"
        self.primary_ability = ("Dexterity", "Wisdom")
        self.saving_throw = ("Strength", "Dexterity")
             
class Paladin(Discipline):
    def __init__(self):
        #Enter stuff here     
        self.description = "A holy warrior bound to a sacred oath"
        self.class_name = "Paladin"
        self.primary_ability = ("Strength", "Charisma")
        self.hit_die = Dice.D10_Roll()
        self.saving_throw = ("Wisdom", "Charisma")
        
class Ranger(Discipline):
    def __init__(self):
        #Enter stuff here 
        self.description = "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization"
        self.class_name = "Ranger"
        self.primary_ability = ("Dexterity", "Wisdom")
        self.hit_die = Dice.D10_Roll()
        self.saving_throw = ("Strength", "Dexterity")
        
class Rogue(Discipline):
    def __init__(self):
        #Enter stuff here 
        self.description = "A scoundrel who uses stealth and trickery to overcome obstacles and enemies"
        self.class_name = "Rogue"
        self.primary_ability = ("Dexterity")
        self.saving_throw = ("Dexterity", "Intelligence")
      
class Sorcerer(Discipline):
    def __init__(self):
        #Enter stuff here 
        self.description = "A spellcaster who draws on inherent magic from a gift or bloodline"
        self.class_name = "Sorcerer"
        self.primary_ability = ("Charisma")
        self.hit_die = Dice.D6_Roll()
        self.saving_throw = ("Constitution", "Charisma")
      
class Warlock(Discipline):
    def __init__(self):
        #Enter stuff here 
        self.description = "A wielder of magic that is derived from a bargain with an extraplanar entity"
        self.class_name = "Warlock"
        self.primary_ability = ("Charisma")
        self.saving_throw = ("Wisdom", "Charisma")
        
class Wizard(Discipline):
    def __init__(self):
        #Enter stuff here 
        self.description = "A scholarly magic-user capable of manipulating the structures of reality"
        self.class_name = "Wizard"
        self.primary_ability = ("Intelligence")
        self.hit_die = Dice.D6_Roll()
        self.saving_throw = ("Intelligence", "Wisdom")
