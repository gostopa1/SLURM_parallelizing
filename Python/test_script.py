# Simple Python script to run as an example
import numpy as np
import scipy.io as sio
import os
a = np.random.randint(10000)
os.makedirs('results',exist_ok = True)
sio.savemat('results/' + str(a)+'.mat', dict(a=a)) # Save MATLAB mat file with the random variable under the name of the variable value