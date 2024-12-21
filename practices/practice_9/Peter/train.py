import numpy as np
def train(data_array, labels):
    num_samples = data_array.shape[0]
    num_features = data_array.shape[1]
    weights = np.zeros((num_features, 1))
    #weights = np.random.rand(num_features)
    for iteration in range(10): # 1000
      #print(f'{synaptic_weights=}') if iteration < 5  else None
      output = 1 / (1 + np.exp(-(np.dot(data_array, weights))))
      error = labels - output
      weights += np.dot(data_array.T, error * output * (1 - output))
      return weights

"""   
    Retrieves an array of NumPy data (normalized, interpolated) and an array/list of labels.
    
    Trains - calculates weight coefficients.
        
    The function returns a one-dimensional array of weights.
"""    
    
    
   

    
