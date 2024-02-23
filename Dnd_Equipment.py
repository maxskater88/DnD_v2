#Dnd for some fun
################################################################################
#
#       IMPORTS
#
################################################################################


################################################################################
#       EQUIPMENT
################################################################################

class Equipment:
    #A skilled artisan can earn one gp per day
    #A single gp can buy a bed-roll, 50ft of rope, or a goat
    #A single sp can buy a flask of lamp oil, a nights rest ina poor inn, or a laborer's work for half a day
    #A single cp can buy a candle, torch, or piece of chalk
    
    coins = {'pp':'Platinum piece(s)', 'gp':'Gold piece(s)', 'ep':'Electrum piece(s)','sp':'Silver piece(s)', 'cp':'Copper piece(s)', }
    
    coin_weight = 1/50 #of a pound
    
    exchange_rates = {'cp':{'cp':1, 'sp':1/10, 'ep':1/50, 'gp':1/100, 'pp':1/1000},
                      'sp':{'cp':10, 'sp':1, 'ep':1/5, 'gp':1/10, 'pp':1/100},  
                      'ep':{'cp':50, 'sp':5, 'ep':1, 'gp':1/2, 'pp':1/20},
                      'gp':{'cp':100, 'sp':0, 'ep':2, 'gp':1, 'pp':1/10},
                      'pp':{'cp':1000, 'sp':100, 'ep':20, 'gp':10, 'pp':1}}
    
    