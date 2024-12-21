import os
import numpy as np
# Open, interpolate and normalize files

x_common = np.linspace(700,1700,20)


def load(folder1, folder2):
  filelist1 = os.listdir(folder1)
  filelist2 = os.listdir(folder2)
  lst1= []
  lst2= []
  for name in filelist1:
    if name.split('.')[1]!='arc_data':
      continue#
    n_interpolated1 = normalize(folder1 + name)
    lst1.append(n_interpolated1)

  for name in filelist2:
    if name.split('.')[1]!='arc_data':
      continue#
    n_interpolated2 = normalize(folder2 + name)
    lst2.append(n_interpolated2)
  combined_array = np.stack(lst1 + lst2)

  lst=[[0 for i in range(12)] + [1 for i in range(9)]]
  labels = np.array(lst).T
  return combined_array, labels

"""   
    Downloading files from folders1, folder2.
    Data normalization, data interpolation to a single step and a single operating range
    
    Possible "subfunctions" are opening a file with normalization and interpolation.
    
    The function returns a two-dimensional NumPy array (which no longer has wavelength data) and a one-dimensional list of labels (labels show type of objects).
"""    
    
    
def test(filename, weights):
    norm = normalize(filename)
    score = 1 / (1 + np.exp(-np.dot(norm, weights)))
    if score > 0.5:
        return "Type B"
    return "Type A"
"""
    Function for calculating the output value for an arbitrary spectrum. Returns '0' or '1', for example.
    
    To do this, it is necessary to obtain a normalized and interpolated spectrum to the desired limits. 
"""
    
    
def normalize(filename):
    spectrum = np.loadtxt(filename, delimiter='\t',encoding='Windows-1251')
    n_interpolated = np.interp(x_common,spectrum[:,0],spectrum[:,1])
    
    return n_interpolated


