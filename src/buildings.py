import sys
import os

def check_game_over(village_matrix):
    for i in range(len(village_matrix)):
        for j in range(len(village_matrix[i])):
            if (village_matrix[i][j] == "T" or village_matrix[i][j] == "C" or village_matrix[i][j] == "H"):
                return
    # return True
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\nVictory!\n")
    sys.exit()

class buildings:
    def __init__(self, max_hp, symbol, coordinates, code):
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.symbol = symbol
        self.coordinates = coordinates
        self.code = code
        # with open("output.txt", "a") as f:
        #         f.write(self.code)
        #         f.write("\n")

    def add_buildings(self, village_matrix, vill_index, hp_matrix):

        for i in range(self.coordinates[0], self.coordinates[1]):
            for j in range(self.coordinates[2], self.coordinates[3]):
                village_matrix[i][j] = self.symbol
                vill_index[i][j] = self.code
                hp_matrix[i][j] = float(self.curr_hp) / float(self.max_hp)

                # with open("output.txt", "a") as f:
                #     f.write(vill_index[i][j])
                #     f.write("\n")

        return village_matrix, vill_index
    
    def building_damage(self, damage, village_matrix, vill_index, hp_matrix):
        self.curr_hp -= damage
        for i in range(self.coordinates[0], self.coordinates[1]):
            for j in range(self.coordinates[2], self.coordinates[3]):
                hp_matrix[i][j] = float(self.curr_hp) / float(self.max_hp)
        if (self.curr_hp <= 0):
            for i in range(self.coordinates[0], self.coordinates[1]):
                for j in range(self.coordinates[2], self.coordinates[3]):
                    village_matrix[i][j] = " "
                    vill_index[i][j] = " "
                    hp_matrix[i][j] = 0
                    check_game_over(village_matrix)
        return village_matrix, vill_index


class town_hall(buildings):
    def __init__(self):
        super().__init__(200, "T", (18, 21, 48, 52), 't')

    def add_town_hall(self, village_matrix, vill_index, hp_matrix):
        village_matrix, vill_index = self.add_buildings(
            village_matrix, vill_index, hp_matrix)
        return village_matrix, vill_index

    def damage(self, damage, village_matrix, vill_index, hp_matrix):
        village_matrix, vill_index = self.building_damage(damage, village_matrix, vill_index, hp_matrix)
        return village_matrix, vill_index


class hut(buildings):
    def __init__(self, coordinates, code):
        super().__init__(30, "H", coordinates, code)

    def add_hut(self, village_matrix, vill_index, hp_matrix):
        village_matrix, vill_index = self.add_buildings(
            village_matrix, vill_index, hp_matrix)
        return village_matrix, vill_index
    
    def damage(self, damage, village_matrix, vill_index, hp_matrix):
        village_matrix, vill_index = self.building_damage(damage, village_matrix, vill_index, hp_matrix)
        return village_matrix, vill_index

class cannon(buildings):
    def __init__(self, coordinates, code):
        super().__init__(150, "C", coordinates, code)
        self.deal_damage = 5

    def add_cannon(self, village_matrix, vill_index, hp_matrix):
        village_matrix, vill_index = self.add_buildings(
            village_matrix, vill_index, hp_matrix)
        return village_matrix, vill_index

    def damage(self, damage, village_matrix, vill_index, hp_matrix):
        village_matrix, vill_index = self.building_damage(damage, village_matrix, vill_index, hp_matrix)
        return village_matrix, vill_index
    
    def attack(self, village_matrix, vill_index, my_troop, hp_matrix):
        enemy_pos = 0
        for i in range(self.coordinates[0]-5, self.coordinates[1]+5):
            for j in range(self.coordinates[2]-5, self.coordinates[3]+5):
                if (village_matrix[i][j] == "B" or village_matrix[i][j] == "K"):
                    enemy_pos = (i, j)
                    break
        if (enemy_pos != 0):
            for i in range(len(my_troop.troop_array)):
                for j in range(len(my_troop.troop_array[i])):
                    if (my_troop.troop_array[i][j].pos == enemy_pos):
                        (my_troop.troop_array[i][j]).troop_damage(self.deal_damage, village_matrix, vill_index, my_troop, hp_matrix)
                        break
        return village_matrix, vill_index


class wall(buildings):
    def __init__(self, coordinates, code):
        super().__init__(50, "W", coordinates, code)

    def add_wall(self, village_matrix, vill_index, hp_matrix):
        village_matrix, vill_index = self.add_buildings(
            village_matrix, vill_index, hp_matrix)
        return village_matrix, vill_index

    def damage(self, damage, village_matrix, vill_index, hp_matrix):
        village_matrix, vill_index = self.building_damage(damage, village_matrix, vill_index, hp_matrix)
        return village_matrix, vill_index