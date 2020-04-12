import numpy as np
from model import Ship

class Population():
    
    def __init__(self):
        self.population = []
        
        for i in range(10):
            self.population.append(Ship())
        
    def update(self):
        for s in self.population:
            s.update()