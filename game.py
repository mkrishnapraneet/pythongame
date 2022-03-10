
import sys

sys.path.insert(0, './src')

from input import *
from village import *
from buildings import *

my_village = village()
# my_buildings = buildings(100, "X", (18,21,48,52))
# my_village.vill = my_buildings.add_buildings(my_village.vill)
twnhall = town_hall()
hut1 = hut((5,8,10,12))
cannon1 = cannon((9,12,21,23))

my_village.vill = twnhall.add_town_hall(my_village.vill)
my_village.vill = hut1.add_hut(my_village.vill)
my_village.vill = cannon1.add_cannon(my_village.vill)

my_village.display()

print("Press any key to continue...")
while True:
    inp = input_to(Get())
    if inp != None:
        break

print("You pressed:", inp)