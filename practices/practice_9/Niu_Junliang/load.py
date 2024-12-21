import os
import numpy as np
# Open, interpolate and normalize files
def load(folder1, folder2):
  path1 = './PbS_spectra/1000/'
  path2 = './PbS_spectra/1170/'
  filelist1 = os.listdir(path1)
  filelist2 = os.listdir(path2)
  lst1= []
  lst2= []
  for name in filelist1:
    if name.split('.')[1]!='arc_data':
      continue#
    spectrum1 = np.loadtxt(path1 + name, delimiter='\t',encoding='Windows-1251')
    x_common1 = np.linspace(700,1700,100)
    n_interpolated1 = np.interp(x_common1,spectrum1[:,0],spectrum1[:,1])
    lst1.append(n_interpolated1 )

  for name in filelist2:
    if name.split('.')[1]!='arc_data':
      continue#
    spectrum2 = np.loadtxt(path2 + name, delimiter='\t', encoding='Windows-1251')
    x_common2 = np.linspace(700,1700,100)
    n_interpolated2 = np.interp(x_common2, spectrum2[:,0], spectrum2[:,1])
    lst2.append(n_interpolated2)
  combined_array = np.stack( lst1 + lst2 )

  lst=[[0 for i in range(12)] + [1 for i in range(9)]]
  labes = np.array(lst).T
  return combined_array, labes

"""   
    Downloading files from folders1, folder2.
    Data normalization, data interpolation to a single step and a single operating range
    
    Possible "subfunctions" are opening a file with normalization and interpolation.
    
    The function returns a two-dimensional NumPy array (which no longer has wavelength data) and a one-dimensional list of labels (labels show type of objects).
"""    
    
    



