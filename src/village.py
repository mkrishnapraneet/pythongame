import numpy as np

class village:
    def __init__(self):
        self.n = 100
        self.m = 40
        self.vill_index = np.empty((self.m,self.n), dtype=object)
        self.vill = np.empty((self.m,self.n), dtype=str)
        
        for i in range(self.n):
            self.vill[0][i] = "*"
        for i in range(1,self.m-1):
            self.vill[i][0] = "*"
            for j in range(1,self.n-1):
                self.vill[i][j] = " "
            self.vill[i][self.n-1] = "*"
        for i in range(self.n):
            self.vill[self.m-1][i] = "*"

        for i in range(len(self.vill_index)):
            for j in range(len(self.vill_index[i])):
                self.vill_index[i][j] = (i*self.n)+j
        # print(self.vill_index)
    
    def display(self):
        for i in range(self.m):
            for j in range(self.n):
                print(self.vill[i][j], end="")
            print()
    
    def buildings(self, town_hall, hut_array, cannon_array, wall_array):
        self.town_hall = [town_hall]
        self.hut_array = hut_array
        self.cannon_array = cannon_array
        self.wall_array = wall_array

        self.building_array = [self.town_hall,self.hut_array,self.cannon_array,self.wall_array]
    
    