import math, cmath
from model import NeuralNetwork


class Ship:
    
    def __init__(self):
        self.x_coord = 100
        self.y_coord = 200
        self.orientation = 0 # angle in radians
        
        self.speed = 10
        
        self.nn = NeuralNetwork()
        
    def update(self, buoy):
        # updates controls
        a,b = self.nn.predict(self.calc_ship_buoy_diff(buoy))      
        self.orientation += a-b
        self.move()
        
    def calc_ship_buoy_angle(self, buoy):
        cangle_ship = cmath.exp(self.orientation * 1j)
        cangle_buoy = complex(buoy.x_coord - self.x_coord,
                              buoy.y_coord - self.y_coord)
        cangle_buoy /= abs(cangle_buoy)
        cangle_diff = cangle_ship * cangle_buoy
        angle_diff = cmath.phase(cangle_diff)
        return angle_diff % math.pi
    
    def calc_ship_buoy_diff(self, buoy):
        return math.sqrt(((buoy.x_coord - self.x_coord) ** 2) + 
                         ((buoy.y_coord - self.y_coord) ** 2)) 
    
    def move(self):
        # update position according to controls
        #☻ self.orientation += 0.1
        cangle = cmath.exp(self.orientation * 1j) # angle in radians
        cspeed = cangle * complex(0, -self.speed)
        x_speed = cspeed.real
        y_speed = cspeed.imag
        
        self.x_coord += x_speed * 1 # delta time factor needed
        self.y_coord += y_speed * 1        
    

        