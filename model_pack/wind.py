import numpy as np

class Wind:
    
    def __init__(self):
        self.x = np.random.uniform(-10, 10)
        self.y = np.random.uniform(-10, 10)
        
    def change_randomly(self, percentage):
        percentage /= 100
        self.x *= np.random.uniform(1 - percentage, 1 + percentage)
        self.y *= np.random.uniform(1 - percentage, 1 + percentage)
        
    def get_view_data(self):
        return {'magnitude': self.magnitude,
                'orientation': self.orientation}