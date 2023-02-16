import matplotlib.pyplot as plt 
import numpy as np 


figure, axis = plt.subplots(3)
plt.tight_layout()
#Carrier sigla
step = 0.01
x = list(np.arange(0,5,step))
x.append(x[-1]+step)
A = 5
f = 5
phase = 0
x = np.array(x)

y = A*np.sin(2*np.pi*f*x+phase)

axis[0].grid(True)
axis[0].plot(x,y,color='blue')
axis[0].set_title('Carrier Signal')

#Main Signal
sig_f = 0.2
#y1 = A*((np.sin(2*np.pi*sig_f*x+phase))**3 + (np.cos(2*np.pi*sig_f*x+phase))**2)
y1 = ((np.sin(3*np.pi*sig_f*x+phase)))

axis[1].grid(True)
axis[1].plot(x,y1,color='green')
axis[1].set_title('Send Signal')

# #Modulated Signal
# y2 = A*np.sin(2*np.pi*(f+y1)*x+phase)
# axis[2].grid(True)
# axis[2].plot(x,y2,color='red')
# axis[2].set_title('Frequency Modulation Signal')

fc = 10 # carrier frequency
k = 0.4 # sensitivity
phi = 2*np.pi*fc*x + k*np.cumsum(y1) # phase
# cim = np.cumsum(y1)
# print(cim[0:100])

sig_mod = np.cos(phi)

axis[2].grid(True)
axis[2].plot(x,sig_mod,color='blue')
axis[2].set_title('Frequency Modulation Signal')

plt.show()

