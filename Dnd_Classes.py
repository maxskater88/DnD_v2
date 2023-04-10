#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import Dnd_Player as  pler
import Dnd_Weapons as weap 
import Dnd_Weapons_MMelee as MM
import Dnd_Weapons_SMelee as SM
import Dnd_Weapons_MRange as MR
import Dnd_Weapons_SRange as SR

################################################################################
#       DICIPLINES (CLASSES)
################################################################################
class Discipline: 
    def __init__(self):
        self.description = ""
        self.class_name = ""
        self.primary_ability = ()
        self.hit_die = pler.player.D8_Roll()
        self.saving_throw = ()
        
class Barbarian(Discipline):
    def __init__(self):
        self.description = "A fierce warrior of primitive background who can enter a battle rage"
        self.class_name = "Barbarian"
        self.primary_ability = ("Strength")
        self.hit_die = pler.player.D12_Roll()
        self.saving_throw = ("Strength", "Constitution")
        self.weapon_prof = SM.Simple_Melee
        self.armor_prof = ['light armor', 'medium armor', 'shields']
        self.weaps_prof = [SM.Simple_Melee, MM.Martial_Melee]
        self.test = 1

class Bard(Discipline):
    def __init__(self):
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
        self.hit_die = pler.player.D10_Roll()
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
        self.hit_die = pler.player.D10_Roll()
        self.saving_throw = ("Wisdom", "Charisma")
        
class Ranger(Discipline):
    def __init__(self):
        #Enter stuff here 
        self.description = "A warrior who uses martial prowess and nature magic to combat threats on the edges of civilization"
        self.class_name = "Ranger"
        self.primary_ability = ("Dexterity", "Wisdom")
        self.hit_die = pler.player.D10_Roll()
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
        self.hit_die = pler.player.D6_Roll()
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
        self.hit_die = pler.player.D6_Roll()
        self.saving_throw = ("Intelligence", "Wisdom")
