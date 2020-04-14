import tkinter as tk

class WindView:
    
    def __init__(self):
        self.grid = 40
        self.wind_views = None
    
    def update(self, canvas, wind): 
        if self.wind_views is not None:
            for wv in self.wind_views:
                canvas.delete(wv)
        
        self.wind_views = []
        for x in range(50):
            for y in range(50):
                wv = canvas.create_line(x * self.grid, y * self.grid, 
                                        x * self.grid + wind.x_vel, 
                                        y * self.grid + wind.y_vel, 
                                        arrow=tk.LAST, fill='gray')
                self.wind_views.append(wv)
 
    def clear(self, canvas):
        for wv in self.wind_views:
            canvas.delete(wv)            
                
                