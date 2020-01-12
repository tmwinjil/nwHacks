import os
import sys
import numpy as np

os.chdir(os.path.dirname(os.path.realpath(sys.argv[0])))
data = np.genfromtxt('train-data/H_FIRE_PNT.csv', dtype=float, delimiter=',', skip_header=1)
