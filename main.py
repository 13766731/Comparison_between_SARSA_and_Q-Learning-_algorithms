# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 17:48:53 2020

@author: a.h
"""
from utils import *

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











        
        
        
        
        