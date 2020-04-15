

class BuoyView:
    
    def __init__(self, index):
        self.size = 10
        self.buoy_view = None
        
        self.index = index + 1
        self.index_view = None
    
    def update(self, canvas, buoy):
        
        if self.buoy_view is None:
            self.buoy_view = canvas.create_oval(buoy.x - (self.size/2),
                                                 buoy.y - (self.size/2),
                                                 buoy.x + (self.size/2),
                                                 buoy.y + (self.size/2), 
                                                 fill='yellow')
        if self.index_view is None:
            self.index_view = canvas.create_text(buoy.x - 12, 
                                                 buoy.y - 12,
                                                 text=self.index,
                                                 font='bold',
                                                 fill='yellow')
        
    def clear(self, canvas):
        canvas.delete(self.buoy_view) 
        self.buoy_view = None
        canvas.delete(self.index_view)
        self.index_view = None