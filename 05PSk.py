import numpy as np
import matplotlib.pyplot as plt

t0 = np.arange(0,2,0.001)
t1 = np.arange(2,4,0.001)
t2 = np.arange(4,6,0.001)
t3 = np.arange(6,8,0.001)
f = 1
y1 = np.sin(2*np.pi*f*t0)
y2 = np.sin(2*np.pi*f*t1*-1)
y3 = np.sin(2*np.pi*f*t2)
y4 = np.sin(2*np.pi*f*t3)
plt.title('Binary PSK for 0100')
plt.plot(t0,y1,color='green')
plt.plot(t1,y2,color='red')
plt.plot(t2,y3,color='green')
plt.plot(t3,y4,color='green')
plt.show()
