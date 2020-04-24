import sys
import numpy as np
import matplotlib.pyplot as plt
from model_pack import Model
from view_pack import View


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()
        
    def run(self):
        """
        Runs evolution for given generations
        """
        generation_count = 50
        self.test_results = [[0] * generation_count for i in range(3)]
        # runs evolution for 200 generations
        for i in range(generation_count):
            display = i > 100            
            self.run_generation(i, display)
         
        t = range(generation_count)
        plt.plot(t, self.test_results[0], 'r')
        plt.plot(t, self.test_results[1], 'g')
        plt.plot(t, self.test_results[2], 'b')        
        plt.show()       
            
        self.model.save('best_ship.npz')
        self.view.mainloop()
  
    def run_generation(self, generation_index, display=False):
        print('------------------------------------------')
        # normal generation evolving in random environment
        print(generation_index, '.generation')
        self.model.prepare_generation()
        self.view.prepare_generation(self.model, display, generation_index)
        self.run_simulation()
        print('')
        self.view.clear()
        self.evaluate()
        self.mutate()
        # testing with 3 test cases
        for test_id in range(3):            
            print('Test case no.', test_id, 'of', generation_index, 
                  '.generation')
            self.model.prepare_test(test_id)            
            self.view.prepare_generation(self.model, display, 
                                         generation_index, test=True)
            time = self.run_simulation(test=True)
            print('Result:', time)
            self.test_results[test_id][generation_index] = time
            self.view.clear()  
        
    def run_simulation(self, test=False):
        """
        Runs simulation by calls model.update() and view.update() methods
        for 1000 time units at most
        """
        for t in range(1000):
            self.model.update(t)
            self.view.update(self.model, t)
            # stop simulation if all ships reached all the targets
            if self.model.population.finished:                
                return t
            if not test:
                message = (str(t + 1) + "/1000 Simulation time |" + 
                           "|" * int(30 * t / 1000) + 
                           "." * int(30 * (1 - (t / 1000))) + "|  ")
                
                sys.stdout.write('\r' + message) 
        return 1000
        
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
    