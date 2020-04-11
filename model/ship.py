import cmath


class Ship:
    
    def __init__(self):
        self.x_coord = 100
        self.y_coord = 200
        self.orientation = 0 # angle in radians
        
        self.speed = 10
        
    def update(self, buoy):
        # updates controls
        
        
        self.move()
    
    def move(self):
        # update position according to controls
        self.orientation += 0.1
        cangle = cmath.exp(self.orientation * 1j) # angle in radians
        cspeed = cangle * complex(0, -self.speed)
        x_speed = cspeed.real
        y_speed = cspeed.imag
        
        self.x_coord += x_speed * 1 # delta time factor needed
        self.y_coord += y_speed * 1        
    

        