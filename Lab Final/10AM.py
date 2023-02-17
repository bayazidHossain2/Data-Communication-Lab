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
message_f = 0.4
message_phase = (np.pi/2)
thita = 2*np.pi*message_f*message_time+message_phase
message_amplitude = message_A*(np.sin(thita)**3-np.cos(thita)**2+np.cos(thita))
axis[1].plot(message_time,message_amplitude)
axis[1].set_title('Message Signal')

#Modulated Signal
modulated_time = np.arange(0,5,0.01)
modulated_amplitude = (carrier_A + message_amplitude)*np.sin(2*np.pi*carrier_f*carrier_time+carrier_phase)
axis[2].plot(modulated_time,modulated_amplitude)
axis[2].set_title('Modulated Signal')

plt.show()