class buildings:
    def __init__(self, max_hp, symbol, coordinates):
        self.max_hp = max_hp
        self.curr_hp = max_hp
        self.symbol = symbol
        self.coordinates = coordinates

    def add_buildings(self, village_matrix):

        for i in range(self.coordinates[0], self.coordinates[1]):
            for j in range(self.coordinates[2], self.coordinates[3]):
                village_matrix[i][j] = self.symbol

        return village_matrix

class town_hall(buildings):

    def __init__(self):
        super().__init__(200, "T", (18, 21, 48, 52))

    def add_town_hall(self, village_matrix):
        village_matrix = self.add_buildings(village_matrix)
        return village_matrix


class hut(buildings):
    def __init__(self, coordinates):
        super().__init__(30, "H", coordinates)

    def add_hut(self, village_matrix):
        village_matrix = self.add_buildings(village_matrix)
        return village_matrix


class cannon(buildings):
    def __init__(self, coordinates):
        super().__init__(150, "C", coordinates)

    def add_cannon(self, village_matrix):
        village_matrix = self.add_buildings(village_matrix)
        return village_matrix

class wall(buildings):
    def __init__(self, coordinates):
        super().__init__(50, "W", coordinates)

    def add_wall(self, village_matrix):
        village_matrix = self.add_buildings(village_matrix)
        return village_matrix
