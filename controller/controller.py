import tkinter as tk
import time
from model import Model
from view import View



class Controller():
    def __init__(self):
        # self.root = tk.Tk()
        self.model = Model()
        self.view = View()
  
    def run(self):
# =============================================================================
#         self.root.title("Sail")
#         self.root.geometry("500x500") 
#         self.root.resizable(0, 0) 
#         self.root.deiconify()
#         self.root.update()
# =============================================================================
        
        
        for i in range(50):
            self.model.update()
            self.view.update(self.model)
            # self.root.update()
            time.sleep(0.2)
        
        self.view.mainloop()
        #self.root.mainloop()
         


if __name__ == '__main__':
    c = Controller()
    c.run()