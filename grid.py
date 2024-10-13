import random

class Grid:
    def __init__(self, sizeX, sizeY, repeatedValue, types, rules) -> None:
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.lst = [[repeatedValue for i in range(sizeX)] for i in range(sizeY)]
        self.types = types
        self.rules = rules

    def get_values(self, coords : tuple) -> list:
        return self.lst[coords[1]][coords[0]]

    def set_values(self, coords : tuple, val : list) -> None:
        self.lst[coords[1]][coords[0]] = val
    
    def get_entropy(self, coords : tuple) -> int:
        return len(self.get_values(coords))
    
    def __repr__(self) -> str:
        return str("\n".join(["".join(["".join(str(len(lst2))) for lst2 in lst]) for lst in self.lst]))
    
    def get_not_collapsed_neighbores(self, coords : tuple) -> list[tuple]:
        res = []
        for x in range(coords[0]-1, coords[0]+2):
            for y in range(coords[1]-1, coords[1]+2):
                if 0 <= x < self.sizeX and 0 <= y < self.sizeY and (x,y) != coords and self.get_entropy((x,y)) != 1:
                    res.append((x,y))
        return res
    
    def get_min_entropy(self,coords_lst : list[tuple]) -> tuple:
        min_entropies = [coords_lst[0]]
        for coords in coords_lst:
            if self.get_entropy(coords) < self.get_entropy(min_entropies[0]) and self.get_entropy(coords) != 1:
                min_entropies = [coords]
            elif self.get_entropy(coords) == self.get_entropy(min_entropies[0]):
                min_entropies.append(coords)
        return random.choice(min_entropies)
    
    def keep_elements_in_common(self,lst1,lst2):
        res = []
        for obj in lst1:
            if obj in lst2:
                res.append(obj)
        return res
    
    def collapse(self, coords : tuple):
        #collapse the state of a cell
        self.set_values(coords, [random.choice(self.get_values(coords))])
        #print(self.get_values(coords))
        
        neighbores = self.get_not_collapsed_neighbores(coords)
        for n_coords in neighbores:
            rules_to_set = self.keep_elements_in_common(self.get_values(n_coords),self.rules[self.get_values(coords)[0]])
            print(rules_to_set)
            self.set_values(n_coords, rules_to_set)
        
        return neighbores
    

#test 

#print(Grid(0,0,0,0,0).keep_elements_in_common([0,1,6,5],[0,6,7]))