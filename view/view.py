import tkinter as tk
import cmath
import time
import view


class View():
    
    GLOBAL_RATIO = 1
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.sidepanel=SidePanel(self.root)
        self.canvas = tk.Canvas(master=self.frame, bg='blue')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        
        
        # self.init_ship()
        self.ship_view = view.ShipView()
        
        
        self.root.title("Sail")
        self.root.geometry("500x500") 
        self.root.resizable(0, 0) 
        self.root.deiconify()
        self.root.update()
        

        
    def update(self, model):
        
        m = model.get_view_data()
        
        # self.update_ship(model.ship)
        self.ship_view.update(self.canvas, model.ship)
        
        # self.update_wind(m['wind'])
        
        self.root.update()
        
    def mainloop(self):
        self.root.mainloop()
        
# =============================================================================
#     def init_ship(self):
#         SIZE = 2
#         # relative coordinates to center
#         shape = [[-4,7],[-4,-3],[0,-8],[4,-3],[4,7]] 
#         # rescale by SIZE
#         self.ship_shape = [[SIZE * j for j in i] for i in shape]
#         self.ship_view = None
#         
#     def update_ship(self, ship):        
#         # offset ship_shape with ship center coordinates
#         coordinates = [[i[0] + ship.x_coord, i[1] + ship.y_coord] for i in self.ship_shape]
#         
#         center = complex(ship.x_coord, ship.y_coord)        
#         cangle = cmath.exp(ship.orientation * 1j) # angle in radians
#         abs_coord = []
#         for x, y in coordinates:
#             cc = cangle * (complex(x, y) - center) + center
#             abs_coord.append([cc.real, cc.imag])
# 
#         if self.ship_view is not None:
#             self.canvas.delete(self.ship_view)        
#         
#         self.ship_view = self.canvas.create_polygon(abs_coord, outline='red', fill='brown')        
#         
#         self.canvas.create_oval(ship.x_coord - 2, ship.y_coord - 2,
#                                 ship.x_coord + 2, ship.y_coord + 2,
#                                 fill='white')
# =============================================================================
        

        
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