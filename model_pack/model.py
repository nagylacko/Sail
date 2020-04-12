from .ship import *
from .population import *
from .buoy import *
from .wind import *


class Model:
 
    def __init__(self):
        self.ship_count = 10
        self.population = Population(self.ship_count)
        self.buoy = Buoy()
        self.wind = Wind()        
        
    def update(self):
        self.population.update(self.buoy)
        

