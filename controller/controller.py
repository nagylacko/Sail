import tkinter as tk
import time
from model import Model
from view import View



class Controller():
    def __init__(self):
        self.model = Model()
        self.view = View()
  
    def run(self):        
        
        for i in range(50):
            self.model.update()
            self.view.update(self.model)
            # self.root.update()
            time.sleep(0.2)
        
        self.view.mainloop()
         


if __name__ == '__main__':
    c = Controller()
    c.run()