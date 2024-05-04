#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################
import random as rnd

################################################################################
#       DICIPLINES (CLASSES)
################################################################################
class Dice:
    def __init__(self):
        self.description = "This is for dice-related stuff"

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
    