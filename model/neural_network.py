import numpy as np
import scipy as sp


class NeuralNetwork:
    
    def __init__(self):
        layer_sizes = [1,4,2]
        
        self.weights = []
        self.biases = []
        for i in range(len(layer_sizes) - 1):
            self.weights.append(np.random.uniform(-0.1, 0.1, size=(layer_sizes[i], layer_sizes[i+1])))
            self.biases.append(np.random.uniform(-0.1, 0.1, size=layer_sizes[i + 1]))
            
    def predict(self, input_layer):
        temp = input_layer
        for w, b in zip(self.weights, self.biases):
            temp = np.matmul(temp, w)
            temp = np.add(temp, b)
        # calculate softmax
        exponentials = np.exp(temp)
        sum_exponentials = sum(exponentials)    
        return exponentials/sum_exponentials        
        
            
    def mutate(self, percentage):
        for w, b in zip(self.weights, self.biases):
            r = 1 - (percentage / 100)
            w *= np.random.uniform(r, 1/r, size=w.shape)
            b *= np.random.uniform(r, 1/r, size=b.shape)            
            
        
        
if __name__ == '__main__':
    
    nn = NeuralNetwork()

    result = nn.predict([10,400])
    print(result)
