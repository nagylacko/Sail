import time
from model_pack import Model
from view_pack import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View(self.model)
  
    def run_generation(self, gen_count): 
        print('gen', gen_count)
        for i in range(100):
            self.model.update(i)
            if gen_count % 3 == 0:
                self.view.update(self.model)
                # time.sleep(0.005)
        time.sleep(1)
        if gen_count % 20:
            self.view.clear()
        
    def evaluate(self):
        self.model.evaluate()
        
    def mutate(self):
        self.model.mutate()               


if __name__ == '__main__':
    c = Controller()
    
    for i in range(100):
        c.run_generation(i)
        c.evaluate()
        c.mutate()        
    
    c.view.mainloop()
    