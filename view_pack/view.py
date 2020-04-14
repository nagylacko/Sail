import tkinter as tk
from .ship_view import ShipView
from .buoy_view import BuoyView
from .wind_view import WindView


class View:
    
    def __init__(self):
        self.root = tk.Tk()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.sidepanel=SidePanel(self.root)
        self.canvas = tk.Canvas(master=self.frame, bg='blue')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.root.title("Sail")
        self.root.geometry("1200x800") 
        self.root.resizable(0, 0) 
        self.root.deiconify()
        self.root.update()
    
    def prepare_generation(self, model):
        self.ship_views = []
        for ship in model.population:
            self.ship_views.append(ShipView())
        self.buoy_views = []
        for buoy in model.buoys:
            self.buoy_views.append(BuoyView())
        self.wind_view = WindView()
        
    def update(self, model):        
        self.wind_view.update(self.canvas, model.wind)
        for ship_view, ship in zip(self.ship_views, model.population):
            ship_view.update(self.canvas, ship)
        for buoy_view, buoy in zip(self.buoy_views, model.buoys):
            buoy_view.update(self.canvas, buoy)        
        self.root.update()
        
    def clear(self):
        for ship_view in self.ship_views:
            ship_view.clear(self.canvas)
        for buoy_view in self.ship_views:
            buoy_view.clear(self.canvas)
        self.wind_view.clear(self.canvas)
        
    def mainloop(self):
        self.root.mainloop() 
        
        
class SidePanel():
    def __init__(self, root):
        self.frame2 = tk.Frame( root )
        self.frame2.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.plotBut = tk.Button(self.frame2, text="Plot ")
        self.plotBut.pack(side="top",fill=tk.BOTH)
        self.clearButton = tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top",fill=tk.BOTH)