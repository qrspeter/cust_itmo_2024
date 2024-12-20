import numpy as np
from colour.plotting import *

RGB = np.array([[79, 52, 45], [87, 22, 67]])

#RGB = colour.models.eotf_inverse_sRGB(np.array([255, 0, 0]) * 255)

plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(RGB)
'''
plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(RGB, 'ITU-R BT.709')
'''
