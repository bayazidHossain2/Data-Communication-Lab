import numpy as np
import matplotlib.pyplot as plt 

figure, axis = plt.subplots(3)
plt.tight_layout()

#carrier Signal 
carrier_time = np.arange(0,5,0.01)
carrier_A = 5
carrier_f = 8
carrier_phase = 0
carrier_amplitude = carrier_A*np.sin(2*np.pi*carrier_f*carrier_time+carrier_phase)
axis[0].plot(carrier_time,carrier_amplitude)
axis[0].set_title('Carrier Signal')

#Message Signal
message_time = np.arange(0,5,0.01)
message_A = 1
message_f = 0.8
message_phase = (np.pi/8)
thita = 2*np.pi*message_f*message_time+message_phase
message_amplitude = message_A*np.cos(thita)
axis[1].plot(message_time,message_amplitude)
axis[1].set_title('Message Signal')

#Modulated Signal
modulated_time = np.arange(0,5,0.01)
moudlated_frequency = 10
k = 0.4 #sensitivity
phi = 2*np.pi*moudlated_frequency*modulated_time + k*np.cumsum(message_amplitude)
modulated_amplitude = np.cos(phi)
axis[2].plot(modulated_time,modulated_amplitude)
axis[2].set_title('Modulated Signal')

plt.show()