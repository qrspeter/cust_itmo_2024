import numpy as np
import matplotlib.pyplot as plt

path = './practice_8_data/sensitivity/'
sens_file = 'S130C_sensitivity_ed.txt'
exper_file = 'spectrum_20241024_144629_ed.txt'

#load data
sens = np.loadtxt(path + sens_file, delimiter='\t')
exper =  np.loadtxt(path + exper_file, delimiter=',')


x = sens[:, 0]

exper_interp = np.interp(x, exper[:, 0], exper[:, 1])

corrected = exper_interp/sens[:, 1]

plt.plot(x, corrected, label='corr')
plt.plot(x, exper_interp, label='orig')
'''
plt.plot(x, corrected/np.max(corrected), label='corr')
plt.plot(x, exper_interp/np.max(exper_interp), label='orig')
'''
plt.xlabel('Wavelenght, nm')
plt.ylabel('Intensity, arb')
plt.legend()
plt.show()







'''
# prepare data
print(list(range(1, 81, 2)))
sens_ed = np.delete(sens, list(range(1, 81, 2)))

print(sens_ed)
print(exper)

print(np.shape(sens_ed))
print(np.shape(exper))
'''

# correct data


# plot original and correted data