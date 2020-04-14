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
    
    def prepare_generation(self, buoys, wind, start_position):
        self.ship_population = []
        for nn in self.nn_population:
            self.ship_population.append(Ship(nn, buoys, wind, start_position))
        
    def update(self, time):
        for ship in self.ship_population:
            ship.update(time)
            
    def evaluate(self):
        ordered_ship_population = sorted(self.ship_population, 
                   key=lambda x: (-x.curr_buoy_index, x.min_distance, x.time))
        ordered_nn_population = []
        for ship in ordered_ship_population:
            ordered_nn_population.append(ship.nn)
            print(ship.curr_buoy_index, ship.min_distance, ship.time) ####################
        self.nn_population = ordered_nn_population
            
    def mutate(self):
        new_nn_population = []        
        
        for nn in self.nn_population[0:3]:
            new_nn_population.append(nn) # elitism
            for i in range(3):
                temp_nn = copy.deepcopy(nn)
                temp_nn.mutate(30) # mutation
                new_nn_population.append(temp_nn)
        self.nn_population = new_nn_population