import tkinter as tk
import cmath


class ShipView:
    
    def __init__(self):
        SIZE = 2
        # relative coordinates to center
        #shape = [[-4,7],[-4,-3],[0,-8],[4,-3],[4,7]] 
        shape = [[-7,-4],[3,-4],[8,0],[3,4],[-7,4]]
        # rescale by SIZE
        self.ship_shape = [[SIZE * j for j in i] for i in shape]
        self.ship_view = None
        
    def update(self, canvas, ship):        
        # offset ship_shape with ship center coordinates
        coordinates = [[i[0] + ship.x_coord, i[1] + ship.y_coord] for i in self.ship_shape]
        
        center = complex(ship.x_coord, ship.y_coord)        
        cangle = cmath.exp(ship.orientation * 1j) # angle in radians
        abs_coord = []
        for x, y in coordinates:
            cc = cangle * (complex(x, y) - center) + center
            abs_coord.append([cc.real, cc.imag])

        if self.ship_view is not None:
            canvas.delete(self.ship_view)        
        
        self.ship_view = canvas.create_polygon(abs_coord, outline='red', fill='brown')        
        
        canvas.create_oval(ship.x_coord - 2, ship.y_coord - 2,
                                ship.x_coord + 2, ship.y_coord + 2,
                                fill='white')