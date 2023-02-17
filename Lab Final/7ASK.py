import numpy as np 
import matplotlib.pyplot as plt

inp_signal = input('Enter binary bit: ')

time = np.array(list())
amplitude = np.array(list())
step = 0
Low_amplitude = 1
High_amplitude = 3

def getSignal(A,time):
    frequency = 2
    phase = 0
    return A*np.sin(2*np.pi*frequency*time+phase)

for i in inp_signal:
    temp_time = np.arange(step,step+2,0.001)
    time = np.append(time,temp_time)
    if i == '0':
        amplitude = np.append(amplitude,getSignal(Low_amplitude,temp_time))
    else:
        amplitude = np.append(amplitude,getSignal(High_amplitude,temp_time))
    step = step + 2

plt.title('ASK Representation of : '+inp_signal)

plt.plot(time,amplitude,color='red')
plt.grid(True)
plt.show()

