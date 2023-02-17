import numpy as np 
import matplotlib.pyplot as plt

inp_signal = input('Enter binary bit: ')

x = list()
y = list()
x.append(0)
y.append(1)

for i in inp_signal:
    if i == '0':
        y.append(y[-1])
    else:
        x.append(x[-1])
        y.append(-1*y[-1])
        y.append(y[-1])
    x.append(x[-1]+1)

plt.title('NRZ I Representation of : '+inp_signal)
plt.plot(x,y,'red')
plt.grid(True)
plt.show()

