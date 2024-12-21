import numpy as np
from colour.plotting import *
'''
RGB = np.array([[79, 52, 45]])# , [87, 22, 67]

#RGB = colour.models.eotf_inverse_sRGB(np.array([255, 0, 0]) * 255)

plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(RGB)

plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(RGB, 'ITU-R BT.709')
'''


cie1931 = 'lin2012xyz2e_5_7sf.csv'
spr = 'led6p3_12v0008.ISD'

path = './color/csv/'


sen = np.loadtxt(path + cie1931, delimiter=',')
spec = np.loadtxt(path + spr, delimiter='\t', skiprows=162)


spec_int = np.interp(sen[:,0], spec[:, 0], spec[:, 1])

comp1 = spec_int*sen[:,1]

x = np.sum(comp1)

print(x)