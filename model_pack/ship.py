import math, cmath
from .neural_network import NeuralNetwork


class Ship:
    
    def __init__(self,neural_network, buoys, wind, start_position):
        self.nn = neural_network
        
        self.buoys = buoys
        self.wind = wind
        
        self.x = start_position['x']
        self.y = start_position['y']
        self.orientation = start_position['orient'] # angle in radians
        
        self.speed = 5        
        
        self.curr_buoy_index = 0
        self.min_distance = self.calc_ship_buoy_dist()
        self.time = 0
        self.finished = False
        
    def update(self, time):
        if self.finished:
            return
        # updates controls by inputs
        steer = self.nn.predict(self.calc_ship_buoy_angle())        
        # moves the ship
        self.move(steer)
        # analyze position
        self.analyze_position(time)        
        
    def calc_ship_buoy_angle(self):
        buoy = self.buoys[self.curr_buoy_index]
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
        self.orientation += steer #speed needs to be included
        # update position according to controls
        cangle = cmath.exp(self.orientation * 1j) # angle in radians
        # cspeed = cangle * complex(0, -self.speed)
        cspeed = cangle * complex(self.speed, 0)
        x_speed = cspeed.real
        y_speed = cspeed.imag
        
        self.x += x_speed * 1 # delta time factor needed
        self.y += y_speed * 1  
        
    def analyze_position(self, time):
        self.min_distance = min(self.calc_ship_buoy_dist(), self.min_distance)
        # min distancen needs to be tuned!!!
        if self.min_distance < 10: 
            self.curr_buoy_index += 1
            if self.curr_buoy_index >= len(self.buoys):
                self.finished = True
                self.min_distance = 0
                self.time = time
                return            
            self.min_distance = self.calc_ship_buoy_dist() 
                
    def calc_ship_buoy_dist(self):
        buoy = self.buoys[self.curr_buoy_index]
        return math.sqrt(((buoy.x - self.x) ** 2) + 
                         ((buoy.y - self.y) ** 2))    
    

        