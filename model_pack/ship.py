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
        self.prev_steer = 0
        
        self.speed = 0        
        
        self.curr_buoy_index = 0
        self.min_distance = self.calc_ship_buoy_dist()
        self.time = 0
        self.finished = False
                
    def update(self, time):
        if self.finished:
            return
        # updates controls by inputs
        controls = self.nn.predict(self.calc_ship_buoy_angle(),
                                   self.calc_ship_wind_angle())
        # moves the ship
        self.move(controls)
        # analyze position
        self.analyze_position(time)                   
        
    def calc_ship_buoy_angle(self):
        buoy = self.buoys[self.curr_buoy_index]
        angle_buoy = cmath.phase(complex(buoy.x - self.x, buoy.y - self.y))
        return self.normalize_angle(angle_buoy - self.orientation)
    
    def calc_ship_wind_angle(self):
        angle_wind = cmath.phase(complex(self.wind.x, self.wind.y)) 
        return self.normalize_angle(angle_wind - self.orientation)
    
    def normalize_angle(self, angle):
        return cmath.phase(cmath.rect(1, angle))
    
    def move(self, controls):
        # update ship speed by wind
# =============================================================================
#         # 135° == 2.356
#         if self.calc_ship_wind_angle() < -2.356 or 2.356 < self.calc_ship_wind_angle():
#             self.speed = 0.5
#         else:
#             # self.speed = min(self.speed, 5)
#             self.speed = 5
# =============================================================================
        wind_angle = self.calc_ship_wind_angle()
        if wind_angle >= 0:
            self.speed = 6 * (math.pi - wind_angle) / math.pi 
        else:
            self.speed = 6 * (wind_angle + math.pi) / math.pi
        self.speed += 1
        # update orientation by steer
        steer = controls['steer']
        if abs(steer) > 0.1: # penalty for turning
            self.speed /= 2
        #print('steer', steer)
        #print('speed', self.speed)
        D = -0.7
        steer += D * (steer - self.prev_steer)
        self.prev_steer = steer
        self.orientation += steer 
        # update position according to controls
        cangle = cmath.exp(self.orientation * 1j) # angle in radians
        # cspeed = cangle * complex(0, -self.speed)
        cspeed = cangle * complex(self.speed, 0)
        x_speed = cspeed.real
        y_speed = cspeed.imag        
        self.x += x_speed
        self.y += y_speed
        
    def analyze_position(self, time):
        self.min_distance = min(self.calc_ship_buoy_dist(), self.min_distance)
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
    

        