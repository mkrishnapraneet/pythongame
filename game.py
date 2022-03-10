
import sys

sys.path.insert(0, './src')

from input import *
from village import *

my_village = village()
my_village.display()

print("Press any key to continue...")
while True:
    inp = input_to(Get())
    if inp != None:
        break

print("You pressed:", inp)