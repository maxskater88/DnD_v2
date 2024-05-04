#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import Dnd_Classes as classes

################################################################################
#       SKILLS
################################################################################

class Skills: 
    
    by_stat = { 'Strength':['Athletics'],
                'Dexterity':['Acrobatics', 'Slight of Hand', 'Stealth'],
                'Intelligence':['Arcana','History','Investigation','Nature','Religion'],
                'Wisdom':['Animal Handling','Insight','Medicine','Perception','Survival'],
                'Charisma':['Deception','Intimidation','Performance','Persuasion']}
    
    strength_check = ''
    dexterity_check = ''
    intelligence_check = ''
    wisdom_check = ''
    charisma_check = ''

class Acrobatics(Skills):
    
    def __init__(self):
        self.primary_stat = 'Dexterity'
        self.description = 'Your Dexterity (Acrobatics) check covers your attempt to stay on your feet in a tricky situation, such as when youre trying to run across a sheet of ice, balance on a tightrope, or stay upright on a rocking ships deck.'

class Animal_Handling(Skills):
    
    def __init__(self):
        self.primary_stat = 'Wisdom'
        self.description = 'When there is any question whether you can calm down a domesticated animal, keep a mount from getting spooked, or intuit an animals intentions, the GM might call for a Wisdom (Animal Handling) check.'
        
class Arcana(Skills):
    
    def __init__(self):
        self.primary_stat = 'Intelligence'
        self.description = 'Your Intelligence (Arcana) check measures your ability to recall lore about spells, magic items, eldritch symbols, magical traditions, the planes of existence, and the inhabitants of those planes.'
        
class Athletics(Skills):
    
    def __init__(self):
        self.primary_stat = 'Strength'
        self.description = 'Your Strength (Athletics) check covers difficult situations you encounter while climbing, jumping, or swimming.'
        
class Deception(Skills):
    
    def __init__(self):
        self.primary_stat = 'Charisma'
        self.description = 'Your Charisma (Deception) check determines whether you can convincingly hide the truth, either verbally or through your actions. This deception can encompass everything from misleading others through ambiguity to telling outright lies.'
        
class History(Skills):
    
    def __init__(self):
        self.primary_stat = 'Intelligence'
        self.description = 'Your Intelligence (History) check measures your ability to recall lore about historical events, legendary people, ancient kingdoms, past disputes, recent wars, and lost civilizations.'
        
class Insight(Skills):
    
    def __init__(self):
        self.primary_stat = 'Wisdom'
        self.description = 'Your Wisdom (Insight) check decides whether you can determine the true intentions of a creature, such as when searching out a lie or predicting someones next move. Doing so involves gleaning clues from body language, speech habits, and changes in mannerisms.'
        
class Intimidation(Skills):
    
    def __init__(self):
        self.primary_stat = 'Charisma'
        self.description = 'When you attempt to influence someone through overt threats, hostile actions, and physical violence, the GM might ask you to make a Charisma (Intimidation) check.'
        
class Investigation(Skills):
    
    def __init__(self):
        self.primary_stat = 'Investigation'
        self.description = 'When you look around for clues and make deductions based on those clues, you make an Intelligence (Investigation) check. You might deduce the location of a hidden object, discern from the appearance of a wound what kind of weapon dealt it, or determine the weakest point in a tunnel that could cause it to collapse. Poring through ancient scrolls in search of a hidden fragment of knowledge might also call for an Intelligence (Investigation) check.'
        
class Medicine(Skills):
    
    def __init__(self):
        self.primary_stat = 'Wisdom'
        self.description = 'A Wisdom (Medicine) check lets you try to stabilize a dying companion or diagnose an illness.'
        
class Nature(Skills):
    
    def __init__(self):
        self.primary_stat = 'Intelligence'
        self.description = 'Your Intelligence (Nature) check measures your ability to recall lore about terrain, plants and animals, the weather, and natural cycles.'
        
class Perception(Skills):
    
    def __init__(self):
        self.primary_stat = 'Wisdom'
        self.description = 'our Wisdom (Perception) check lets you spot, hear, or otherwise detect the presence of something. It measures your general awareness of your surroundings and the keenness of your senses.'
        
class Performance(Skills):
    
    def __init__(self):
        self.primary_stat = 'Charisma'
        self.description = 'Your Charisma (Performance) check determines how well you can delight an audience with music, dance, acting, storytelling, or some other form of entertainment.'
        
class Persuasion(Skills):
    
    def __init__(self):
        self.primary_stat = 'Charisma'
        self.description = 'When you attempt to influence someone or a group of people with tact, social graces, or good nature, the GM might ask you to make a Charisma (Persuasion) check.'
        
class Religion(Skills):
    
    def __init__(self):
        self.primary_stat = 'Intelligence'
        self.description = 'Your Intelligence (Religion) check measures your ability to recall lore about deities, rites and prayers, religious hierarchies, holy symbols, and the practices of secret cults.'
        
class Slight_of_Hand(Skills):
    
    def __init__(self):
        self.primary_stat = 'Dexterity'
        self.description = 'Whenever you attempt an act of legerdemain or manual trickery, such as planting something on someone else or concealing an object on your person, make a Dexterity (Sleight of Hand) check.'
        
class Survival(Skills):
    
    def __init__(self):
        self.primary_stat = 'Wisdom'
        self.description = 'The GM might ask you to make a Wisdom (Survival) check to follow tracks, hunt wild game, guide your group through frozen wastelands, identify signs that owlbears live nearby, predict the weather, or avoid quicksand and other natural hazards.'
        
class Stealth(Skills):
    
    def __init__(self):
        self.primary_stat = 'Dexterity'
        self.description = 'Make a Dexterity (Stealth) check when you attempt to conceal yourself from enemies, slink past guards, slip away without being noticed, or sneak up on someone without being seen or heard.'
        