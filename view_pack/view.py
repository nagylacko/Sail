import tkinter as tk
from view_pack import ShipView, BuoyView, WindView


class View:
    
    GLOBAL_RATIO = 1
    
    def __init__(self, model):
        self.root = tk.Tk()
        
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.sidepanel=SidePanel(self.root)
        self.canvas = tk.Canvas(master=self.frame, bg='blue')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        self.ship_views = []
        for i in range(model.ship_count):
            self.ship_views.append(ShipView())
        self.buoy_view = BuoyView()
        self.wind_view = WindView()
        
        self.root.title("Sail")
        self.root.geometry("500x500") 
        self.root.resizable(0, 0) 
        self.root.deiconify()
        self.root.update()
        
    def update(self, model):        
        
        self.wind_view.update(self.canvas, model.wind)
        for sv, s in zip(self.ship_views, model.population):
            sv.update(self.canvas, s)
        self.buoy_view.update(self.canvas, model.buoy)        
        self.root.update()
        
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