import numpy as np
import matplotlib.pyplot as plt

w = np.arange(0,20*np.pi,0.01)
plt.plot(w,np.cos(w),color='red')
plt.plot(w,np.sin(w),color='blue')
plt.plot(w,0*w,color='black')
plt.show()

print(w)
