from model import Population, Wind
from model import Ship # for a single ship



class Model():
 
    def __init__(self):
        self.ship = Ship() # for a single ship
        self.population = Population()
        self.wind = Wind()
        
        
    def update(self):
        self.ship.update()
        
  
  
    def get_view_data(self):
        return {'population': self.population,
                'wind': self.wind}
