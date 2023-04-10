#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################


################################################################################
#       WEAPONS
################################################################################
class Weapons:
    wepon_types = ("Simple Melee Weapons",     "Simple Ranged Weapons", 
                   "Martial Melee Weapons",    "Martial Ranged Weapons")
    
    simple_melee = ("Club",         "Dagger",      "GreatClub",   "HandAxe",  
                    "Javelin",      "LightHammer", "Mace",        "Quaterstaff",  
                    "Sickle",       "Spear")
    
    simple_range = ("LightCrossbow","Dart",        "Shortbow",    "Sling")
    
    martial_melee = ("BattleAxe", "Flail",       "Glaive",        "GreatAxe", 
                    "GreatSword", "Halberd",     "Lance",         "Longsword", 
                    "Maul",       "Morningstar", "Pike",          "Rapier", 
                    "Scimitar",   "Shortsword",  "Trident",       "Warpick", 
                    "Warhammer",  "Whip")
    
    martial_range = ("Blowgun",   "HandCrosbow", "HeavyCrossbow", "Longbow", 
                     "Net")
    weapons_dict = {wepon_types[0]: simple_melee,
                    wepon_types[1]: simple_range,
                    wepon_types[2]: martial_melee,
                    wepon_types[3]: martial_range}
               
    def __init__(self):
        pass
    
