import numpy as np
import matplotlib.pyplot as plt

while True:
    num = int(input('Enter the number of frequency :'))
    t = np.arange(0,2*num*np.pi,0.001)
    A = 2
    f = 1
    delta = 0
    y = A*np.sin(f*t+delta)
    plt.plot([0,20],[0,0],color='blue')
    plt.plot([0,0],[-3,3],color='blue')
    plt.xlabel('Time')
    plt.ylabel('Amplitude')
    plt.title('Simple signal show')
    plt.grid(True)
    plt.plot(t,y,color='red')
    plt.show()
