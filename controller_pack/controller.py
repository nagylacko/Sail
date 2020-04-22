import sys
import time
import numpy as np
from model_pack import Model
from view_pack import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
  
    def run_generation(self, display, generation_index, test=False):
        print('------------------------------------------')
        if not test:
            print(generation_index, '.generation')
            self.model.prepare_generation()
            self.view.prepare_generation(self.model, display, generation_index)
        else:
            print('Test')
            self.model.prepare_test(0)
            self.view.prepare_generation(self.model, display)
        for i in range(1000):
            self.model.update(i)
            self.view.update(self.model)
            if self.model.population.finished:
                break
            message = (str(i+1) + "/1000 Simulation time |" + 
                       "|" * int(30 * i / 1000) + 
                       "." * int(30 * (1 - (i / 1000))) + "|  ")
            sys.stdout.write('\r' + message)
        print('')
        self.view.clear()    
        
    def evaluate(self):
        self.model.evaluate()
        
    def mutate(self):
        self.model.mutate() 
          

if __name__ == '__main__':
    """
    Main function
    """
    np.random.seed(0)
    c = Controller()
    
    generation_count = 200
    for i in range(generation_count):
        display = test = False
        if i > 15:
            display = test = True            
        c.run_generation(display, i)
        c.evaluate()
        c.mutate()

        
    c.model.save('best_ship.npz')
     
# =============================================================================
#     c.model.load('best_ship.npz', 1)
#     
#     generation_count = 200
#     simulation_time = 10000
#     for i in range(generation_count):
#         gui = True
#         c.run_generation(gui, i, simulation_time)
# =============================================================================                   
  
    c.view.mainloop()
    