
def Reward(state_now):
    if state_now == 0:
        R=1
    if state_now != 0:
        R=-1
    if (state_now > 5)  or  (state_now < -5):
        print('We are in Danger area')
        R=-10
    return R