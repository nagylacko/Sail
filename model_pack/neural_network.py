import numpy as np
import scipy as sp


class NeuralNetwork:
    
    def __init__(self):
        layer_sizes = [1,4,1]
        
        self.weights = []
        self.biases = []
        for i in range(len(layer_sizes) - 1):
            self.weights.append(np.random.uniform(-0.1, 0.1, size=(layer_sizes[i], layer_sizes[i+1])))
            self.biases.append(np.random.uniform(-0.1, 0.1, size=layer_sizes[i + 1]))
            
    def predict(self, ship_buoy_angle, ship_speed):
        layer = np.array([ship_buoy_angle])
        for w, b in zip(self.weights, self.biases):
            layer = np.matmul(layer, w)
            layer = np.add(layer, b)
            layer = np.tanh(layer)
        # calculate softmax
        # exponentials = np.exp(x)
        # sum_exponentials = sum(exponentials)    
        # return exponentials/sum_exponentials   
        #return {'steer': layer[0], 'speed': layer[1]}
        return {'steer': layer[0]}
            
    def mutate(self, percentage):
        r = 1 - (percentage / 100)
        for w, b in zip(self.weights, self.biases):
            w *= np.random.uniform(r, 1/r, size=w.shape)
            b *= np.random.uniform(r, 1/r, size=b.shape)
            
    def save(self, filename):
        np.savez_compressed(filename, 
                            weights=np.array(self.weights), 
                            biases=np.array(self.biases))
        
    def load(self, filename):
        file = np.load(filename, allow_pickle=True)
        self.weights = file['weights']
        self.biases = file['biases']
        

