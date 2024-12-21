import os
import numpy as np


def load_and_normalize_files(folder1, folder2):
    path0 = './practice_9_data/PbS_spectra/1000'
    path1 = './D/practice_9_data/PbS_spectra/1240'
    filelist1 = os.listdir(path0)
    filelist2 = os.listdir(path1)
    lst1 = []
    lst2 = []
    for name in filelist1:
        if name.split('.')[1]!= 'arc_data':
            continue
        spectrum = np.loadtxt(path0 + '/' + name)
        x_common = np.linspace(700, 1700, 100)
        n_interpolated = np.interp(x_common, spectrum[:, 0], spectrum[:, 1])
        lst1.append(n_interpolated)
    for name in filelist2:
        if name.split('.')[1]!= 'arc_data':
            continue
        spectrum = np.loadtxt(path1 + '/' + name)
        x_common = np.linspace(700, 1700, 100)
        n_interpolated = np.interp(x_common, spectrum[:, 0], spectrum[:, 1])
        lst2.append(n_interpolated)
    combined_array = np.stack((lst1, lst2))
    lst = []
    for i in range(12):
        for j in range(12):
            lst.append(np.array([i, j]).T)
    labs = np.array(lst).T
    return combined_array, labs