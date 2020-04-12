import numpy as np
from .ship import Ship

class Population:
    
    def __init__(self, ship_count):
        self.population = []        
        for i in range(ship_count):
            self.population.append(Ship())
            
    def __iter__(self):
        return self.population.__iter__()    
        
    def update(self, buoy):
        for s in self.population:
            s.update(buoy)