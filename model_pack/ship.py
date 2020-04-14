import math, cmath
from .neural_network import NeuralNetwork


class Ship:
    
    def __init__(self, mode):
        self.x = 100
        self.y = 200
        self.orientation = -(math.pi / 2) # angle in radians
        
        self.speed = 5
        
        if mode == 'random_nn':
            self.nn = NeuralNetwork()
        
        self.min_distance = 100000 ##########
        self.time = 10000 ###################
        
    def update(self, buoys, time):
        # updates controls by inputs
        steer = self.nn.predict(self.calc_ship_buoy_angle(buoys[0]))        
        # move the ship
        self.move(steer)
        # record distance
        self.record_distance(buoys[0], time)        
        
    def calc_ship_buoy_angle(self, buoy):
        cangle_buoy = complex(buoy.x - self.x, buoy.y - self.y)
        angle_buoy = cmath.phase(cangle_buoy)
        angle_diff = angle_buoy - self.orientation
        angle_diff %= (2 * math.pi)
        if angle_diff > math.pi:
            return -2 * math.pi + angle_diff
        if angle_diff < -math.pi:
            return 2 * math.pi - angle_diff 
        return angle_diff
    
    def move(self, steer):
        # update orientation by steer
        self.orientation += steer
        # update position according to controls
        cangle = cmath.exp(self.orientation * 1j) # angle in radians
        # cspeed = cangle * complex(0, -self.speed)
        cspeed = cangle * complex(self.speed, 0)
        x_speed = cspeed.real
        y_speed = cspeed.imag
        
        self.x += x_speed * 1 # delta time factor needed
        self.y += y_speed * 1  
        
    def calc_ship_buoy_dist(self, buoy):
        return math.sqrt(((buoy.x - self.x) ** 2) + 
                         ((buoy.y - self.y) ** 2))
        
    def record_distance(self, buoy, time):
        self.min_distance = min(self.calc_ship_buoy_dist(buoy), self.min_distance)
        if self.min_distance < 3: # needs to be tuned
            self.min_distance = 0
            self.time = time
            
    def mutate(self, percentage):
        self.nn.mutate(percentage)
    

        