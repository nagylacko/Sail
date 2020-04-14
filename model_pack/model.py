import math
from .ship import Ship
from .population import Population
from .buoys import Buoys
from .wind import Wind


class Model:
 
    def __init__(self):
        self.population_count = 9
        self.population = Population(self.population_count)

    def prepare_generation(self):
        self.buoys = Buoys()
        self.wind = Wind()
        start_position = {'x': 100, 'y': 200, 'orient': -(math.pi / 2)}
        self.population.prepare_generation(self.buoys, self.wind, start_position)        
        
    def update(self, time):
        self.population.update(time)
        
    def evaluate(self):
        self.population.evaluate()
        
    def mutate(self):
        self.population.mutate()
        

