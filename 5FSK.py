import numpy as np
import matplotlib.pyplot as plt


data = input('Enter the digital Data:')
amplitude = 5
low_frequency = 1
high_frequency = 2
phase = 0

y = np.array([])
time = np.array([])
start = 0
for x in data:
    
    t_time = np.arange(start,start+2,0.001)
    if x is '0':
        t_y =   amplitude*np.sin(2*np.pi*low_frequency*t_time+phase)
    else:
        t_y =   amplitude*np.sin(2*np.pi*high_frequency*t_time+phase)
    y = np.append(y,t_y)
    time = np.append(time,t_time)
    start = start+2
plt.grid()
plt.title('FSK for '+data)
plt.plot(time,y,color='red')
plt.show()