import numpy as np
def train(data_array, labels):
    num_samples = data_array.shape[0]
    num_features = data_array.shape[1]
    weights = np.zeros(num_features)
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
    
    
   
    
def test(test_spectrum, weights):
    score = np.dot(spectrum, weights)
    if score > 0.5:
        return "Type A"
    return "Type B"
"""
    Function for calculating the output value for an arbitrary spectrum. Returns '0' or '1', for example.
    
    To do this, it is necessary to obtain a normalized and interpolated spectrum to the desired limits. 
"""
    
    
