import math
import numpy as np
from .population import Population
from .buoys import Buoys
from .wind import Wind


class Model:
 
    def __init__(self):
        self.population_count = 50
        self.population = Population(self.population_count)

    def prepare_generation(self):
        buoy_count = np.random.randint(4,9)
        print('Buoy count:', buoy_count)
        self.buoys = Buoys(buoy_count)
        self.wind = Wind()
        start_position = {'x': np.random.uniform(100, 1060), 
                          'y': np.random.uniform(100, 650), 
                          'orient': np.random.uniform(0, 2 * math.pi)}
        self.population.prepare_generation(self.buoys, self.wind, 
                                           start_position)        
        
    def update(self, time):
        self.population.update(time)
        
    def evaluate(self):
        self.population.evaluate()
        
    def mutate(self):
        self.population.mutate()
        
    def save(self, filename):
        self.population.save(filename)
        
    def load(self, filename, number):
        self.population.load(filename, number)
        

