import numpy as np


class NeuralNetwork:
    """
    The neural network which controls the ship
    """    
    def __init__(self):
        """
        Randomly initializes the neural network parameters
        The layers of the network are hard-coded
        """
        layer_sizes = [2,6,4,1]        
        self.weights = []
        self.biases = []
        for i in range(len(layer_sizes) - 1):
            self.weights.append(np.random.uniform(-0.1, 0.1, size=(layer_sizes[i], layer_sizes[i+1])))
            self.biases.append(np.random.uniform(-0.1, 0.1, size=layer_sizes[i + 1]))
            
    def predict(self, ship_buoy_angle, wind_angle):
        """
        Predicts the controls of the by the environment
        Parameters:
        - ship_buoy_angle : float - the angle in radians betwween target buoy
                            and ship
        - wind_angle : float - the angle in radians betwween wind and ship
        Returns:
        - dictionary - contains the controls of the ship
        Side effects:
        - None
        """
        layer = np.array([ship_buoy_angle, wind_angle])
        for w, b in zip(self.weights, self.biases):
            layer = np.matmul(layer, w)
            layer = np.add(layer, b)
            layer = np.tanh(layer)
        return {'steer': layer[0]}
            
    def mutate(self, percentage):
        """
        Mutates the neural network by multiplying all the weights and biases
        with a random number around 1 and between the percentage values
        Parameters:
        - percentage : int - sepcifies the magnitude of mutation in percentage
        Returns:
        - None
        Side effects:
        - Updates all values of self.weights and self.biases
        """
        r = 1 - (percentage / 100)
        for w, b in zip(self.weights, self.biases):
            w *= np.random.uniform(r, 1/r, size=w.shape)
            b *= np.random.uniform(r, 1/r, size=b.shape)
            
    def save(self, filename):
        """
        Saves the neural network into .npz file
        """
        np.savez_compressed(filename, 
                            weights=np.array(self.weights), 
                            biases=np.array(self.biases))
        
    def load(self, filename):
        """
        Loads neural network from .npz file
        """
        file = np.load(filename, allow_pickle=True)
        self.weights = file['weights']
        self.biases = file['biases']
        

