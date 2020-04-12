from model import Population, Wind, Buoy
from model import Ship # for a single ship



class Model():
 
    def __init__(self):
        self.ship = Ship() # for a single ship
        self.population = Population()
        self.buoy = Buoy()
        self.wind = Wind()
        
        
    def update(self):
        self.ship.update(self.buoy) # for a single ship
        self.population.update()
        

