# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:48:53 2020

@author: a.h
"""

from pybrain.tools.customxml.networkreader import NetworkReader
from numpy import loadtxt
import scipy.io as sio
import numpy as np
import random
import  matplotlib.pyplot as plt


################ Load the system 
reference = NetworkReader.readFrom('compressor.xml') 
mean_input_refrence = 300.013641
mean_output_reference = 18.292426
alpha = 0.8
gama = 0.6

########################## Action & State
actions=list(range(-5,6)) 
state=list(range(0,11)) 
Q=np.zeros((np.size(state),np.size(actions)))
######################### Functions 

def Reward(state_now):
    if state_now == 0:
        R=1
    if state_now != 0:
        R=-1
    if (state_now > 5)  or  (state_now < -5):
        print('We are in Danger area')
        R=-10
    return R

epsilon=0.2
def Policy(Q,S):
     if random.uniform(0, 1) < epsilon:
        A=random.randint(-5,5)
        return A
     else:
      for i in range(np.size(actions)):
        a=Q[S,i]
        b=max(Q[S,:])
        if  a >= b:
            A=i
            return A-5    
        
def State(output_plant, output_reference):
   
    error = output_reference - output_plant
    if (error < -5) or (error > 5):
        state_now = 10
    if (error >= -5) and (error <= 5):
        state_now = 9
    if (error >= -4) and (error <= 4):
        state_now = 8
    if (error >= -3) and (error <= 3):
        state_now = 7
    if (error >= -2) and (error <= 2):
        state_now = 6
    if (error >= -1) and (error <= 1):
        state_now = 5
    if (error >= -0.8) and (error <= 0.8):
        state_now = 4
    if (error >= -0.4) and (error <= 0.4):
        state_now = 3
    if (error >= -0.2) and (error <= 0.2):
        state_now = 2
    if (error >= -0.1) and (error <= 0.1):
        state_now = 1
    if error == 0:
        state_now = 0
    return (state_now)

def plant(inpute,fault):
    mean_input_refrence = 300.013641
    mean_output_reference = 18.292426
    inpute += fault
    a=reference.activate([inpute/mean_input_refrence])*mean_output_reference
    return (a)
########################### inputs

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





for i in inpute_test:
    S=10
    n += 1
    while S >= 2:
        print(i)
        A=Policy(Q,S)
        action = i + A
        output_plant = plant(action,fault)
        output_reference = reference.activate([i/mean_input_refrence])*mean_output_reference
        error += ((output_reference - output_plant)**2)
        S_perim=State(output_plant,output_reference)
        R=Reward(S_perim)
        Q[S,A]=Q[S,A]+alpha*(R+gama* max(Q[S_perim,:])-Q[S,A])
        S=S_perim
        loop_number += 1
        if S <= 2:
            LOOP_number_Q[n] =  loop_number
            loop_number = 0
            MSE_Q[n] = error / np.size(inpute_test)
            error = 0
            



########################### Loop SARSA

error = 0 
loop_number_sarsa = 0
n = -1
MSE_sarsa = np.zeros(np.size(inpute_test))
LOOP_number_sarsa= np.zeros(np.size(inpute_test))

Q=np.zeros((np.size(state),np.size(actions)))

for i in inpute_test:
    S=10
    A=Policy(Q,S)
    n += 1
    while S >= 2:
        print(i)
        action = i + A
        output_plant = plant(action,fault)
        output_reference = reference.activate([i/mean_input_refrence])*mean_output_reference
        error += ((output_reference - output_plant)**2)
        S_perim=State(output_plant,output_reference)
        R=Reward(S_perim)
        A_perim=Policy(Q,S_perim)
        Q[S,A]=Q[S,A]+alpha*(R+gama* Q[S_perim,A_perim]-Q[S,A])
        S=S_perim
        A=A_perim
        loop_number += 1
        if S <= 2:
           
            LOOP_number_sarsa[n] =  loop_number
            loop_number = 0
            MSE_sarsa[n] = error / np.size(inpute_test)
            error = 0
            
            

############################# Results


plt.figure(1)
plt.plot(inpute_test,LOOP_number_sarsa)
plt.plot(inpute_test,LOOP_number_Q,'r')
plt.xlabel('time')
plt.ylabel('mass flow')











        
        
        
        
        