import sys

# sys.path.insert(0, '../')
from village import *

class troop:
    def __init__(self, max_hp, damage, symbol, village_matrix):
        self.damage = damage
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.symbol = symbol




class king(troop):
    def __init__(self, village_matrix):
        super().__init__(50, 10, "K", village_matrix)

    def spawn(self, village_matrix, spawn_pos):
        if (int(spawn_pos) == 1):
            self.pos = (38, 25)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        elif (int(spawn_pos) == 2):
            self.pos = (38, 75)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        else:
            self.pos = (1, 50)
            village_matrix[self.pos[0]][self.pos[1]] = "K"

    def move(self, village_matrix, direction):
        if (direction == "w" and village_matrix[self.pos[0]-1][self.pos[1]] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0]-1, self.pos[1])
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        elif (direction == "a" and village_matrix[self.pos[0]][self.pos[1]-1] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0], self.pos[1]-1)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        elif (direction == "s" and village_matrix[self.pos[0]+1][self.pos[1]] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0]+1, self.pos[1])
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        elif (direction == "d" and village_matrix[self.pos[0]][self.pos[1]+1] == " "):
            village_matrix[self.pos[0]][self.pos[1]] = " "
            self.pos = (self.pos[0], self.pos[1]+1)
            village_matrix[self.pos[0]][self.pos[1]] = "K"

    def display_health(self):
        print("\nKing's Health: \n")
        # print(game.hut_array)
        for i in range(self.max_hp):
            print("#", end="")
        print("\n")
    
    def attack(self, village_matrix, vill_index, my_village):
        if (village_matrix[self.pos[0]-1][self.pos[1]] == "H" or village_matrix[self.pos[0]-1][self.pos[1]] == "C" or village_matrix[self.pos[0]-1][self.pos[1]] == "W" or village_matrix[self.pos[0]-1][self.pos[1]] == "T" ):
            code = vill_index[self.pos[0]-1][self.pos[1]]
            print(code)
            # with open("output.txt", "a") as f:
            #     f.write(code)
            #     f.write("\n")

            required_building = 0

            for i in range(len(my_village.building_array)):
                for j in range(len(my_village.building_array[i])):
                    # print(my_village.building_array[i][j])
                    # with open("output.txt", "a") as f:
                    #     f.write(str(my_village.building_array[i][j]))
                    #     f.write("\n")
                    if (my_village.building_array[i][j].code == code):
                        required_building = my_village.building_array[i][j]
                        break
            village_matrix, vill_index = required_building.damage(self.damage, village_matrix, vill_index)
            with open("output.txt", "a") as f:
                f.write(required_building.code)
                f.write("\n")

        return village_matrix, vill_index

