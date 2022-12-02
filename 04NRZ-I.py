import numpy as np
import matplotlib.pyplot as plt

def getSignal(bits):
    x_co = []
    y_co = []
    x_co.append(0)
    y_co.append(1)
    x = 1
    for bit in bits:
        if bit is '1':
            if y_co[-1] is 1:
                x_co.append(x-1)
                y_co.append(-1)
                y_co.append(-1)
            else:
                x_co.append(x-1)
                y_co.append(1)
                y_co.append(1)
        else:
            y_co.append(y_co[-1])
        x_co.append(x)
        x = x+1
    print('x is :',x_co)
    print('Y is :',y_co)
    return [x_co,y_co]


#Wev Ploting
#plt.plot([0,1,1,2,2,3,3,4,5,5,6,7,8,8,9,9,10,10],[1,1,0,0,1,1,0,0,0,1,1,1,1,0,0,1,1,0],color='red')
while True:
    inp = input('Enter your digital signal :')
    sig = getSignal(inp)

    #Axis Ploting
    plt.title("NRZ-I Digital to Digital conversion :")
    plt.xlabel('Input signal is :'+inp)
    plt.scatter(np.arange(0,len(inp)+1,1),[0]*(len(inp)+1),color='pink')
    plt.plot([0,len(inp)+2],[0,0],color='blue')
    plt.plot([0,0],[-1.5,1.5],color='blue')
    plt.plot(sig[0],sig[1],color='red')
    plt.show()
