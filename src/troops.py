class troop:
    def __init__(self, max_hp, damage, symbol, village_matrix, spawn_pos):
        self.damage = damage
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.symbol = symbol
        

class king(troop):
    def __init__(self, village_matrix, spawn_pos):
        super().__init__(50, 10, "K", village_matrix, spawn_pos)
        if (int(spawn_pos) == 1):
            self.pos = (38,25)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        elif (int(spawn_pos) == 2):
            self.pos = (38,75)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        else:
            self.pos = (1,50)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        


        