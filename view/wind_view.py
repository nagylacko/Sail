import tkinter as tk

class WindView:
    
    def __init__(self):
        self.grid = 40
        self.wind_view_list = None
    
    def update(self, canvas, wind): 
        if self.wind_view_list is not None:
            for wv in self.wind_view_list:
                canvas.delete(wv)
        
        self.wind_view_list = []
        for x in range(50):
            for y in range(50):
                wv = canvas.create_line(x * self.grid, y * self.grid, 
                                        x * self.grid + wind.x_vel, 
                                        y * self.grid + wind.y_vel, 
                                        arrow=tk.LAST, fill='gray')
                self.wind_view_list.append(wv)
 
                
                
                