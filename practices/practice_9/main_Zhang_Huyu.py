import numpy as np
import sys

sys.path.insert(0, './Zhang_Huyu')
import load
import train


if __name__ == "__main__":
    path0 = 'practice_9_data\\PbS_spectra\\1000'
    path1 = 'practice_9_data\\PbS_spectra\\1240'
    inpData, labs = load.load(path0, path1)
    weights = train.train(inpData, labs)
    test_file = ''
    train.test(test_file, weights)