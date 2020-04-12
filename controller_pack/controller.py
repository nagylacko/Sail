import time
from model_pack import Model
from view_pack import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self.model)
  
    def run(self):        
        for i in range(100):
            self.model.update()
            self.view.update(self.model)
            time.sleep(0.2)
        
        self.view.mainloop()     


if __name__ == '__main__':
    c = Controller()
    c.run()
    
    