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
        self.label = tk.Label(self.top_frame, text='X. Generation', font=("Arial Bold", 20), width=80)
        self.label.pack(side='bottom', fill=None, expand=False)
        
        # Left Frame with Controls
        self.left_frame = tk.Frame(self.root)
        self.left_frame.pack(side='left', fill=None, expand=False, padx=10, pady=5)
        
        self.next_gen_but = tk.Button(self.left_frame, text="Next Generation", padx=5, pady=5)
        self.next_gen_but['command'] = lambda: self.stop_update()
        self.next_gen_but.pack(side='top')
        
        
        self.clear_button = tk.Button(self.left_frame, text="Clear", padx=5, pady=5)
        self.clear_button.pack()
        self.info_label = tk.Label(self.left_frame, text='info label', bg='yellow', height=42, padx=10, pady=10)
        self.info_label.pack(side='bottom')
        
        # Right Frame with Canvas
        self.right_frame = tk.Frame(self.root)
        self.right_frame.pack(fill=None, expand=False)
        self.canvas = tk.Canvas(master=self.right_frame, width=1160, height=750, bg='blue')
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=1)  
        
        self.root.update()
            
    def prepare_generation(self, model, display, generation_index=-1):
        """
        Initializes all view objects for display
        """
        self.display = display
        if generation_index == -1:
            self.label['text'] = 'Test'
        else:
            self.label['text'] = str(generation_index) + '. generation'
        self.wind_view = WindView(self.canvas, model.wind)
        self.ship_views = []
        for s in model.population:
            self.ship_views.append(ShipView())
        self.buoy_views = []
        for i, buoy in enumerate(model.buoys):
            self.buoy_views.append(BuoyView(self.canvas, buoy, i))        
        self.root.update()
        
    def stop_update(self):
        self.display = False
        
    def update(self, model):
        """
        Calls update method of all view objects        
        Updates and displays only 10 ship_views at most
        """
        if not self.display:
            return        
        for i in range(min(len(self.ship_views), 10)): 
            self.ship_views[i].update(self.canvas, model.population[i])
        self.root.update()
        
    def clear(self):
        for ship_view in self.ship_views:
            ship_view.clear(self.canvas)
        for buoy_view in self.buoy_views:
            buoy_view.clear(self.canvas)
        self.wind_view.clear(self.canvas)
        
    def mainloop(self):
        self.root.mainloop() 

       
        