# Find color coordinates for spectra of Carbon dots LED and place then on the chromaticity diagram CIE1931

import numpy as np
import colour.plotting as cl
import matplotlib.pyplot as plt

x_min, x_max, step = 380, 830, 1
cmf = 'lin2012xyz2e_5_7sf.csv'
spectra = 'led6p3_12v0008.ISD' # 11, 13, 21, 52
csv_dir = './csv/'

def integrate(f, step):
    area = np.sum(f)*step
    return area  
    
    
def rgbcalc(cmf, spectra, step):
    a = []
    for i in range(3):
        c = cmf[i]*spectra
        a.append(integrate(c, step))
        
    return tuple(a) 
    
def loadfiles(file_cmf,file_spect):
    cmf_o = np.loadtxt(file_cmf, delimiter=',')
    sp_o = np.loadtxt(file_spect,delimiter='\t',skiprows = 212)
    x_sp_o,y_sp_o=sp_o[:,0], sp_o[:,1]
    x_interp=np.arange(x_min,x_max+1,step)
    x_cmf_o = cmf_o[:,0]
    y_sp_interp = np.interp(x_interp,x_sp_o,y_sp_o)
    y_cmf_o=cmf_o[:,0]
    y_cmf_interp=[]
    for i in range(1, 4):
        y_cmf_interp.append(np.interp(x_interp,x_cmf_o,cmf_o[:,i]))
    return(y_cmf_interp) # y_sp_interp returns nothing, I should return both arrays or use 2 different functions.      
    
cmf_o = np.loadtxt(csv_dir + cmf, delimiter=',')
sp_o = np.loadtxt(csv_dir + spectra, delimiter='\t', skiprows = 212)
x_sp_o, y_sp_o = sp_o[:, 0], sp_o[:, 1]
x_interp = np.arange(x_min, x_max + 1, step)
y_sp_interp = np.interp(x_interp, x_sp_o, y_sp_o)
x_cmf_o = cmf_o[:, 0]
y_cmf_interp = []

for i in range(1, 4):
    y_cmf_interp.append(np.interp(x_interp, x_cmf_o, cmf_o[:, i]))
arr = rgbcalc(y_cmf_interp, y_sp_interp, step)

RGB = np.array(arr) # not sure of it is correct
cl.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(RGB)