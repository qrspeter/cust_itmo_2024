import numpy as np
import sys

sys.path.insert(0, './Niu_Junliang')
import load
import train
    

if __name__ == "__main__":
    path1 = './PbS_spectra/1000/'
    path2 = './PbS_spectra/1170/'

    inpdata,labes = load.load(path1,path2)


    weights =train.train(inpdata,labes)

    test.file='training_example.py'
    train.test(test.file,weights)
    '''
    Get the folder addresses for data A and B.
    
    Import training data A and B, and create a data array and a markup list/array - call the load.load() function.
    
    Training and getting weights - calling the test.test() function.
    
    Obtaining the test spectrum and type determination (A or B)
    
    '''