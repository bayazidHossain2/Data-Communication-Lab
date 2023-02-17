import numpy as np 
import matplotlib.pyplot as plt

inp_signal = input('Enter binary bit: ')

x = list()
y = list()
for i in inp_signal:
    if i == '0':
        y.append(-1)
        y.append(0)
    else:
        y.append(1)
        y.append(0)
y.append(y[-1])
print('y : ',y)
plt.title('Return Zero Representation of : '+inp_signal)
#plt.plot(x,y,'red')
x = np.arange(0,len(y))
plt.step(x,y,color='green',where='post')
plt.grid(True)
plt.show()

