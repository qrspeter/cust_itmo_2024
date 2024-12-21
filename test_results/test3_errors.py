import numpy as np

var1 = [5, 1, 6, 7, 18, 8, 14, 2, 6, 2, 12, 3]
var2 = [1, 1, 8, 1, 5, 1, 3, 0, 18, 1]
errors1 = 41
errors2 = 47
problems = 10

var = [var1, var2]
errors = [errors1, errors2]

for i, j in zip(var, errors):
    result = problems -  np.round(np.array(i) * problems / j)
    print(result, np.mean(result))
    
