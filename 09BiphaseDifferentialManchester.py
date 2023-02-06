import numpy as np
import matplotlib.pyplot as plt

def getSignal(bits):
    y = list()
    if bits[0] == '0':
        y.append(-1)
        y.append(1)
    else:
        y.append(1)
        y.append(-1)
    for i in range(1,len(bits)):
        if bits[i] is '1':
            y.append(y[-1])
            y.append(-1*y[-2])
        else:
            y.append(-1*y[-1])
            y.append(y[-2])
    return y

#Wev Ploting
#plt.plot([0,1,1,2,2,3,3,4,5,5,6,7,8,8,9,9,10,10],[1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0],color='red')
while True:
    inp = input('Enter your digital signal :')

    if(inp is ''):
        break
    y = list()
    for ch in inp:
        if ch is '0':
            y.append(0)
        else:
            y.append(1)
    
    y.append(0)
    x = np.arange(0,len(inp)+1,1)
    print('y is :',y)
    figure, axis = plt.subplots(2)
    # For Unipolar Representation
    axis[0].grid(True)
    axis[0].step(x,y,where='post')
    axis[0].set_title("Unipolar Representation of \'"+inp+"\'")

    sig = getSignal(inp)
    # For  representation
    axis[1].grid(True)
    x = np.arange(0,len(sig))
    axis[1].step(x,sig,color='red',where='post')
    axis[1].set_title("Diffrential Manchaster representation of \'"+inp+"\'")
    plt.show()
