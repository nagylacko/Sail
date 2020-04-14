import copy
from .ship import Ship

class Population:
    
    def __init__(self, ship_count):
        self.population = []        
        for i in range(ship_count):
            self.population.append(Ship(mode='random_nn'))
            
    def __iter__(self):
        return self.population.__iter__()    
        
    def update(self, buoys, time):
        for ship in self.population:
            ship.update(buoys, time)
            
    def evaluate(self):
        self.population = sorted(self.population, key = lambda x: (x.min_distance, x.time))
            
    def mutate(self):
        new_population = []        
        
        for ship in self.population[0:3]:
            ship.__init__(mode='')
            new_population.append(ship) # elitism
            for i in range(3):
                temp_ship = copy.deepcopy(ship)
                temp_ship.__init__(mode='')
                temp_ship.mutate(30) # mutation
                new_population.append(temp_ship)
        self.population = new_population