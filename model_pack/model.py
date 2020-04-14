from .ship import *
from .population import *
from .buoy import *
from .wind import *


class Model:
 
    def __init__(self):
        self.ship_count = 9
        self.population = Population(self.ship_count)
        self.buoys = Buoys()
        self.wind = Wind()        
        
    def update(self, time):
        self.population.update(self.buoys, time)
        
    def evaluate(self):
        self.population.evaluate()
        
    def mutate(self):
        self.population.mutate()
        

