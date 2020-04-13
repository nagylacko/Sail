

class BuoyView:
    
    def __init__(self):
        self.size = 8
        self.buoy_view = None
    
    def update(self, canvas, buoy):
        
        if self.buoy_view is None:
             self.buoy_view = canvas.create_oval(buoy.x_coord - (self.size/2),
                                                 buoy.y_coord - (self.size/2),
                                                 buoy.x_coord + (self.size/2),
                                                 buoy.y_coord + (self.size/2), 
                                                 fill = 'yellow')
        
    def clear(self, canvas):
        canvas.delete(self.buoy_view) 
        self.buoy_view = None