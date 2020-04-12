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
            
    def predict(self, input_layer):
        layer = np.array([input_layer])
        for w, b in zip(self.weights, self.biases):
            layer = np.matmul(layer, w)
            layer = np.add(layer, b)
            layer = np.tanh(layer)
        # calculate softmax
        # exponentials = np.exp(x)
        # sum_exponentials = sum(exponentials)    
        # return exponentials/sum_exponentials   
        return layer[0]        
            
    def mutate(self, percentage):
        for w, b in zip(self.weights, self.biases):
            r = 1 - (percentage / 100)
            w *= np.random.uniform(r, 1/r, size=w.shape)
            b *= np.random.uniform(r, 1/r, size=b.shape)         
        

