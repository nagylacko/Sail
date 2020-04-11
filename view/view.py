import tkinter as tk
import cmath
import time


class View():
    
    GLOBAL_RATIO = 1
    
    def __init__(self):
        self.master = tk.Tk()
        
        self.frame = tk.Frame(self.master)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.sidepanel=SidePanel(self.master)
        self.canvas = tk.Canvas(master=self.frame, bg='blue')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        
        self.ball = self.canvas.create_oval(0,0,100,100, fill='red')
        
        self.init_ship()
        
        
        self.master.title("Sail")
        self.master.geometry("500x500") 
        self.master.resizable(0, 0) 
        self.master.deiconify()
        self.master.update()
        

        
    def update(self, model):
        xspeed = 5
        yspeed = 0        
        self.canvas.move(self.ball, xspeed, yspeed)
        
        m = model.get_view_data()
        self.update_ship(model.ship)
        # self.update_wind(m['wind'])
        
        self.master.update()
        
    def mainloop(self):
        self.master.mainloop()
        
    def init_ship(self):
        SIZE = 2
        # relative coordinates to center
        rel_coord = [[-4,7],[-4,-3],[0,-8],[4,-3],[4,7]] 
        # rescale by SIZE
        self.ship_rel_coord = [[SIZE * j for j in i] for i in rel_coord]
        self.ship = None
        
    def update_ship(self, ship):
        
        # offset with ship center coordinates
        coordinates = [[i[0] + ship.x_coord, i[1] + ship.y_coord] for i in self.ship_rel_coord]
        
        center = complex(ship.x_coord, ship.y_coord)
        
        cangle = cmath.exp(ship.orientation * 1j) # angle in radians
        abs_coord = []
        for x, y in coordinates:
            v = cangle * (complex(x, y) - center) + center
            abs_coord.append([v.real, v.imag])


        if self.ship is not None:
            self.canvas.delete(self.ship)              
        
        
        self.ship = self.canvas.create_polygon(abs_coord, 
                                   outline='red', fill='brown')
        
        
# =============================================================================
#         e = 10
#         self.canvas.create_rectangle(ship.x_coord - e, ship.y_coord - e,
#                                      ship.x_coord + e, ship.y_coord + e, 
#                                      outline='red', fill='brown')
# =============================================================================
        
        
        self.canvas.create_oval(ship.x_coord - 2, ship.y_coord - 2,
                                ship.x_coord + 2, ship.y_coord + 2,
                                fill='white')
        
    def update_ship_rect(self, ship):
        e = 10 #rectangle edge length half
        self.canvas.create_rectangle(ship.x_coord - e, ship.y_coord - e,
                                     ship.x_coord + e, ship.y_coord + e, 
                                     outline='red', fill='brown')
        
    def update_wind(self, wind):
        grid = 30
        for x in range(10):
            for y in range(10):
                self.canvas.create_line(x * grid, y * grid, 
                                        x * grid + wind.x_vel, 
                                        y * grid + wind.y_vel, 
                                        arrow=tk.LAST, fill='red')
        
        
class SidePanel():
    def __init__(self, root):
        self.frame2 = tk.Frame( root )
        self.frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.plotBut = tk.Button(self.frame2, text="Plot ")
        self.plotBut.pack(side="top",fill=tk.BOTH)
        self.clearButton = tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top",fill=tk.BOTH)