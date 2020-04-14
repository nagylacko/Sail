

class BuoyView:
    
    def __init__(self):
        self.size = 8
        self.buoy_view = None
    
    def update(self, canvas, buoys):
        
        if self.buoy_view is None:
             self.buoy_view = canvas.create_oval(buoys[0].x - (self.size/2),
                                                 buoys[0].y - (self.size/2),
                                                 buoys[0].x + (self.size/2),
                                                 buoys[0].y + (self.size/2), 
                                                 fill = 'yellow')
        
    def clear(self, canvas):
        canvas.delete(self.buoy_view) 
        self.buoy_view = None