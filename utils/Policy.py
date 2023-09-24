
import random
import numpy as np

def Policy(Q,S, epsilon, actions):
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