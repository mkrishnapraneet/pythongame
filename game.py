
import sys
import os

from time import sleep

sys.path.insert(0, './src')

from input import *
from village import *
from buildings import *
from troops import *

my_village = village()
# my_buildings = buildings(100, "X", (18,21,48,52))
# my_village.vill = my_buildings.add_buildings(my_village.vill)
twnhall = town_hall()

hut1 = hut((5,7,10,12))
hut2 = hut((32,34,10,12))
hut3 = hut((5,7,85,87))
hut4 = hut((32,34,85,87))
hut5 = hut((32,34,49,51))

cannon1 = cannon((9,12,21,23))
cannon2 = cannon((9,12,76,78))

wall1 = wall((21,22,40,41))
wall2 = wall((22,23,41,42))
wall3 = wall((23,24,42,43))
wall4 = wall((20,21,39,40))

wall5 = wall((21,22,59,60))
wall6 = wall((22,23,58,59))
wall7 = wall((23,24,57,58))
wall8 = wall((20,21,60,61))

wall9 = wall((15,16,47,48))
wall10 = wall((15,16,48,49))
wall11 = wall((15,16,49,50))
wall12 = wall((15,16,50,51))
wall13 = wall((15,16,51,52))
wall14 = wall((15,16,52,53))


my_village.vill = twnhall.add_town_hall(my_village.vill)

my_village.vill = hut1.add_hut(my_village.vill)
my_village.vill = hut2.add_hut(my_village.vill)
my_village.vill = hut3.add_hut(my_village.vill)
my_village.vill = hut4.add_hut(my_village.vill)
my_village.vill = hut5.add_hut(my_village.vill)

my_village.vill = cannon1.add_cannon(my_village.vill)
my_village.vill = cannon2.add_cannon(my_village.vill)

my_village.vill = wall1.add_wall(my_village.vill)
my_village.vill = wall2.add_wall(my_village.vill)
my_village.vill = wall3.add_wall(my_village.vill)
my_village.vill = wall4.add_wall(my_village.vill)

my_village.vill = wall5.add_wall(my_village.vill)
my_village.vill = wall6.add_wall(my_village.vill)
my_village.vill = wall7.add_wall(my_village.vill)
my_village.vill = wall8.add_wall(my_village.vill)

my_village.vill = wall9.add_wall(my_village.vill)
my_village.vill = wall10.add_wall(my_village.vill)
my_village.vill = wall11.add_wall(my_village.vill)
my_village.vill = wall12.add_wall(my_village.vill)
my_village.vill = wall13.add_wall(my_village.vill)
my_village.vill = wall14.add_wall(my_village.vill)

my_king = king(my_village.vill)
king_deployed = 0
# my_village.display()
while (1):
    inp = input_to(Get())
    os.system('cls' if os.name == 'nt' else 'clear')    
    if (inp == "1" or inp == "2" or inp == "3"):
        if (king_deployed == 0):
            my_king.spawn(my_village.vill, inp)
            king_deployed = 1
    elif (inp == "w" or inp == "a" or inp == "s" or inp == "d"):
        if (king_deployed == 1):
            my_king.move(my_village.vill, inp)
    elif (inp == 'q'):
        break
    my_village.display()
    my_king.display_health()
    
    sleep(0.1)
    


# print("Press any key to continue...")
# while True:
#     inp = input_to(Get())
#     if inp != None:
#         break

# print("You pressed:", inp)