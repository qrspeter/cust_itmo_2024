'''
based on 
https://www.geeksforgeeks.org/how-to-load-and-save-3d-numpy-array-to-file-using-savetxt-and-loadtxt-functions/
https://www.tutorialspoint.com/how-to-load-and-save-3d-numpy-array-file-using-savetxt-and-loadtxt-functions

numpy reshape:
numpy.reshape(a, /, shape=None, order='C', *, newshape=None, copy=None)[source]
Gives a new shape to an array without changing its data.
https://numpy.org/doc/stable/reference/generated/numpy.reshape.html
'''

import numpy as np

filename = __file__[:-2] + 'txt'

arr3d = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
            [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
            [[19, 20, 21], [22, 23, 24], [25, 26, 27]]], dtype='int8')
            
print(arr3d)

arr_reshaped = arr3d.reshape(arr3d.shape[0], -1)

print(arr_reshaped)

np.savetxt(filename, arr_reshaped, fmt='%d')




loaded_arr = np.loadtxt(filename)
 
loaded_arr3d = loaded_arr.reshape(
    loaded_arr.shape[0], loaded_arr.shape[1] // arr3d.shape[2], arr3d.shape[2])
    
print(loaded_arr3d)

# check if both arrays are same or not:
if (loaded_arr3d == arr3d).all():
    print("Yes, both the arrays are same")
else:
    print("No, both the arrays are not same")