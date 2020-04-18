import copy
from .ship import Ship
from .neural_network import NeuralNetwork

class Population:
    
    def __init__(self, population_count):
        self.nn_population = []        
        for i in range(population_count):
            self.nn_population.append(NeuralNetwork())
            
    def __iter__(self):
        return self.ship_population.__iter__()  
    
    def __getitem__(self, index):
        return self.ship_population[index]
    
    def __len__(self):
        return len(self.ship_population)
    
    def prepare_generation(self, buoys, wind, start_position):
        self.finished = False
        self.ship_population = []
        for nn in self.nn_population:
            self.ship_population.append(Ship(nn, buoys, wind, start_position))
        
    def update(self, time):
        for ship in self.ship_population:
             ship.update(time)                 
        self.finished = all([ship.finished for ship in self.ship_population])
            
    def evaluate(self):
        ordered_ship_population = sorted(self.ship_population, 
                   key=lambda x: (-x.curr_buoy_index, x.min_distance, x.time))
        ordered_nn_population = []
        for ship in ordered_ship_population:
            ordered_nn_population.append(ship.nn)            
        self.nn_population = ordered_nn_population
        for i in range(5):
            ship = ordered_ship_population[i]
            print(ship.curr_buoy_index, round(ship.min_distance, 2), ship.time) #!!!
            
    def mutate(self):
        new_nn_population = []        
        
        for nn in self.nn_population[0:5]:
            new_nn_population.append(nn) # elitism
            for i in range(9):
                temp_nn = copy.deepcopy(nn)
                temp_nn.mutate(30) # mutation
                new_nn_population.append(temp_nn)
        self.nn_population = new_nn_population
        
    def save(self, filename):
        self.nn_population[0].save(filename)
        
    def load(self, filename, number):
        self.nn_population = []
        for i in range(number):
            nn = NeuralNetwork()
            nn.load(filename)
            self.nn_population.append(nn)
        self.mutate()
        
        