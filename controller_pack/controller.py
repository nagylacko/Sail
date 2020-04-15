import time
from model_pack import Model
from view_pack import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
  
    def run_generation(self, gui, generation_count, sim_time): 
        print(generation_count, ' .generation')
        self.model.prepare_generation()
        if gui:
            self.view.prepare_generation(self.model)
        for i in range(sim_time):
            self.model.update(i)
            if gui:
                self.view.update(self.model)
                #time.sleep(0.005)
            if self.model.population.finished:
                break
        if gui:
           self.view.clear()
        
    def evaluate(self):
        self.model.evaluate()
        
    def mutate(self):
        self.model.mutate()               


if __name__ == '__main__':
    c = Controller()
    
    for i in range(80):
        gui = True if i % 10 == 0 else False
        if i < 60:
            gui = False
        c.run_generation(gui, i, 800)
        c.evaluate()
        c.mutate() 
            
    c.view.mainloop()
    