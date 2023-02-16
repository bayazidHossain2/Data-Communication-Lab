import numpy as np
import matplotlib.pyplot as plt


data = input('Enter the digital Data:')
amplitude = 5
f = 1
phase = 0

y = np.array([])
time = np.array([])
start = 0
for x in data:
    
    t_time = np.arange(start,start+2,0.001)
    if x is '0':
        t_y =   amplitude*np.sin(2*np.pi*f*t_time+phase)
    else:
        t_y =   amplitude*np.sin(2*np.pi*f*t_time*(-1)+phase)
    y = np.append(y,t_y)
    time = np.append(time,t_time)
    start = start+2
plt.grid()
plt.title('PSK for '+data)
plt.plot(time,y,color='blue')
plt.show()

# t0 = np.arange(0,2,0.001)
# t1 = np.arange(2,4,0.001)
# t2 = np.arange(4,6,0.001)
# t3 = np.arange(6,8,0.001)
# f = 1
# y1 = np.sin(2*np.pi*f*t0)
# y2 = np.sin(2*np.pi*f*t1*-1)
# y3 = np.sin(2*np.pi*f*t2)
# y4 = np.sin(2*np.pi*f*t3)
# plt.title('Binary PSK for 110011')
# plt.plot(t0,y1,color='green')
# plt.plot(t1,y2,color='red')
# plt.plot(t2,y3,color='green')
# plt.plot(t3,y4,color='green')
# plt.show()