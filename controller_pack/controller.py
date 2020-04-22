import sys
import numpy as np
from model_pack import Model
from view_pack import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
  
    def run_generation(self, display, generation_index, simulation_time):
        # this function must be rethinked!!!!!!!!!!!!!!!!!!
        print('------------------------------------------')
        print(generation_index, '.generation')
        self.model.prepare_generation()
        self.view.prepare_generation(self.model, display, generation_index)
        for i in range(simulation_time):
            self.model.update(i)
            self.view.update(self.model)
            if self.model.population.finished:
                break
            message = (str(i+1) + "/" + str(simulation_time) + " Tick of simulation [" + "|" * int(30 * i / simulation_time) + " " * int(30 * (1 - (i / simulation_time))) + "]  ")
            sys.stdout.write('\r' + message)
        print('')
        self.view.clear()
        
    def evaluate(self):
        self.model.evaluate()
        
    def mutate(self):
        self.model.mutate()               


if __name__ == '__main__':
    np.random.seed(0)
    c = Controller()
    
    generation_count = 200
    simulation_time = 1000
    for i in range(generation_count):
        display = False
        if i > 3:
            display = True
        c.run_generation(display, i, simulation_time)
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
    