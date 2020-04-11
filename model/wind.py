import numpy as np

class Wind:
    
    def __init__(self):
        self.magnitude = 1
        self.orientation = 0
        self.x_vel = -10
        self.y_vel = -10
        
    def change_randomly(self, percentage):
        percentage /= 100
        self.magnitude *= np.random.uniform(1 - percentage, 1 + percentage)
        self.orientation *= np.random.uniform(1 - percentage, 1 + percentage)
        
    def get_view_data(self):
        return {'magnitude': self.magnitude,
                'orientation': self.orientation}