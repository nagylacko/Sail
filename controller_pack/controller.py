import sys
import numpy as np
from model_pack import Model
from view_pack import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        
    def run(self):
        generation_count = 200
        test_cases = 3
        self.test_results = [[]] * test_cases
        for i in range(generation_count):
            display = False
            if i > 15:
                display = True            
            self.run_generation(i, display, test=False)
            self.evaluate()
            self.mutate()
            if i > 15:
                for j in range(test_cases):
                    self.run_generation(i, display=True, test=True, test_id=j)    
            
        self.model.save('best_ship.npz')
        self.view.mainloop()
  
    def run_generation(self, generation_index, display=False, test=False, 
                       test_id=-1):
        print('------------------------------------------')
        if test:
            # testing
            print('Test case no.', test_id, 'of', generation_index, 
                  '.generation')
            self.model.prepare_test(test_id=test_id)
        else:
            # normal generation evolving in random environment
            print(generation_index, '.generation')
            self.model.prepare_generation()
        self.view.prepare_generation(self.model, display, generation_index, 
                                     test)
        # updating the model for 1000 time unit at most
        for t in range(1000):
            self.model.update(t)
            self.view.update(self.model, t)
            if self.model.population.finished:
                # stop simulation if all ships reached all the targets
                if test:
                    pass
                    ##self.test_results[test_id].append(t)
                break
            message = (str(t + 1) + "/1000 Simulation time |" + 
                       "|" * int(30 * t / 1000) + 
                       "." * int(30 * (1 - (t / 1000))) + "|  ")
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
    c.run()
    

     
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
    