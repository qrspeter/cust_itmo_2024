# Find color coordinates for spectra of Carbon dots LED and place then on the chromaticity diagram CIE1931

import numpy as np
import colour.plotting as cl
import matplotlib.pyplot as plt

x_min, x_max, step = 380, 830, 1
cmf = 'lin2012xyz2e_5_7sf.csv'
spectra = 'led6p3_12v0008.ISD' # 11, 13, 21, 52
csv_dir = './csv/'

def integrate(f, step):
    area = np.sum(cmf[:,f])*step
    return area  
    
    
def rgbcalc(cmf, spectra, step):
    a = []
    for i in range(1,4):
        a = cmf[:,i]*spectra
        a.append(integral(a, step))
        
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
    for i in range(3):
        y_cmf_interp.append(np.interp(x_interp,x_cmf_o,cmf_o[:,i+1]))
    return(y_cmf_interp) # а вот y_sp_interp нигде не возвращается, то ли возвращать кортежем оба массива, то ли двумя разными функциями открывать.      
    
cmf_o = np.loadtxt(csv_dir + cmf, delimiter=',')
sp_o = np.loadtxt(csv_dir + spectra, delimiter='\t', skiprows = 212)
x_sp_o, y_sp_o = sp_o[:, 0], sp_o[:, 1]
x_interp = np.arange(x_min, x_max + 1, step)
y_sp_interp = np.interp(x_interp, x_sp_o, y_sp_o)
x_cmf_o = cmf_o[:, 0]
y_cmf_interp = []

for i in range(3):
    y_cmf_interp.append(np.interp(x_interp, x_cmf_o, cmf_o[:, i + 1]))
arr = rgbcalc(y_cmf_interp, y_sp_interp, step)

RGB = np.array(arr) # если такая конвертация допустима
cl.plot_RGB_chromaticities_in_chromaticity_diagram_CIE1931(RGB)