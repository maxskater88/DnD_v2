#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import Dnd_Player as  pler
#import Dnd_Classes as disp
#import Dnd_Races as   rces
#import Dnd_Weapons as weap

################################################################################
#       MAIN
################################################################################
player1 = pler.player()
player2 = pler.player()
print(player1.race.race_mod)
print(player1.race.description)
print(player1.discipline.class_name)
print(player1.base_stats)
print(pler.player.D10_Roll())
#End of File