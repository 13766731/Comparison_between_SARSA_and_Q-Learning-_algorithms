        
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