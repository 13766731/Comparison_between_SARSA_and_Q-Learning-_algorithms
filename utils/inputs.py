
from pybrain.tools.customxml.networkreader import NetworkReader
import numpy as np
import scipy.io as sio

reference = NetworkReader.readFrom('compressor.xml') 
mean_input_refrence = 300.013641
mean_output_reference = 18.292426
alpha = 0.8
gama = 0.6
epsilon=0.2
########################## Action & State
actions=list(range(-5,6)) 
state=list(range(0,11)) 
Q=np.zeros((np.size(state),np.size(actions)))

data1=sio.loadmat('input.mat')
inpute1=data1['input_compressor']# velocity of system
inpute_test=inpute1[:100]        
        
########################### Loop Q
error = 0 
loop_number = 0
n = -1
MSE_Q = np.zeros(np.size(inpute_test))
LOOP_number_Q = np.zeros(np.size(inpute_test))
fault = 1.1
