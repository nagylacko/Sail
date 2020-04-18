import tkinter as tk
from .ship_view import ShipView
from .buoy_view import BuoyView
from .wind_view import WindView


class View:
    
    def __init__(self):
        # Main Window
        self.root = tk.Tk()               
        self.root.title("Sail")
        self.root.geometry("1300x800") 
        self.root.resizable(0, 0) 
        self.root.deiconify()
        
        # Top Frame with Label
        self.top_frame = tk.Frame(self.root)
        self.top_frame.pack(side=tk.TOP, fill=None, expand=False)
        self.label = tk.Label(self.top_frame, text='X. Generation', font=("Arial Bold", 20), width=80, bg='yellow')
        self.label.pack(side='bottom', fill=None, expand=False)
        
        # Left Frame with Controls
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side='left', fill=None, expand=False, padx=10, pady=5)
        
        self.next_gen_but = tk.Button(self.left_frame, text="Next Generation", padx=5, pady=5)
        self.next_gen_but['command'] = lambda: self.stop_update()
        self.next_gen_but.pack(side='top')
        self.clear_button = tk.Button(self.left_frame, text="Clear", padx=5, pady=5)
        self.clear_button.pack()
        self.info_label = tk.Label(self.left_frame, text='info label', bg='yellow', height=30, padx=10, pady=10)
        self.info_label.pack(side='bottom')
        
        # Right Frame with Canvas
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(fill=None, expand=False)
        self.canvas = tk.Canvas(master=self.right_frame, width=1100, height=750, bg='blue')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)       

        
        self.root.update()
            
    def __init__old(self):
        self.root = tk.Tk()
        
        # Main Frame with Canvas
        self.frame = tk.Frame(self.root)
        self.frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)        
        self.canvas = tk.Canvas(master=self.frame, bg='blue')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        
        # Secondary Frame with Buttons
        self.frame2 = tk.Frame(self.root)
        self.frame2.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)       
        self.plotBut = tk.Button(self.frame2, text="Stop")
        self.plotBut['command'] = lambda: self.stop_update()
        self.plotBut.pack(side="top",fill=tk.BOTH)
        self.clearButton = tk.Button(self.frame2, text="Clear")
        self.clearButton.pack(side="top",fill=tk.BOTH)        

        # Main Window settings        
        self.root.title("Sail")
        self.root.geometry("1200x800") 
        self.root.resizable(0, 0) 
        self.root.deiconify()
        self.root.update()
    
    def prepare_generation(self, model):
        self.stop_display = False
        self.ship_views = []
        for i in range(len(model.population)):
            self.ship_views.append(ShipView())
        self.buoy_views = []
        for i, buoy in enumerate(model.buoys):
            self.buoy_views.append(BuoyView(i))
        self.wind_view = WindView()
        
    def stop_update(self):
        self.stop_display = True
        
    def update(self, model):
        """
        Calls update method of all view objects        
        Updates and displays only 20 ship_views at most
        """
        if self.stop_display:
            return
        self.wind_view.update(self.canvas, model.wind)
        for i in range(min(len(self.ship_views), 20)): 
            self.ship_views[i].update(self.canvas, model.population[i])
        for buoy_view, buoy in zip(self.buoy_views, model.buoys):
            buoy_view.update(self.canvas, buoy)        
        self.root.update()
        
    def clear(self):
        for ship_view in self.ship_views:
            ship_view.clear(self.canvas)
        for buoy_view in self.buoy_views:
            buoy_view.clear(self.canvas)
        self.wind_view.clear(self.canvas)
        
    def mainloop(self):
        self.root.mainloop() 


if __name__ == "__main__":
    v = View()
        
        