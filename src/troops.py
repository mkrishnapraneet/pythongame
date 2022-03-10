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
            self.pos = (38,25)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        elif (int(spawn_pos) == 2):
            self.pos = (38,75)
            village_matrix[self.pos[0]][self.pos[1]] = "K"
        else:
            self.pos = (1,50)
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
        print("\nKing's Health: ")
        for i in range(self.max_hp):
            print("#", end="")
        print("\n")
    # def attack(self, village_matrix):



        