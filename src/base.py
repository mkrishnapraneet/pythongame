# import numpy as np

# class base_grid:
#     def __init__(self):
#         self.n = 100
#         self.m = 100
#         self.vill_index = np.zeros((self.m,self.n), dtype=int)
#         self.vill = np.empty((self.m,self.n), dtype=str)
#         for i in range(self.n):
#             self.vill[0][i] = "H"
#         for i in range(1,self.m-1):
#             self.vill[i][0] = "I"
#             for j in range(1,self.n-1):
#                 self.vill[i][j] = " "
#             self.vill[i][self.n-1] = "I"
#         for i in range(self.n):
#             self.vill[self.m-1][i] = "H"
    
#     def display(self):
#         for i in range(self.m):
#             for j in range(self.n):
#                 print(self.vill[i][j], end="")
#             print()
    
    
    