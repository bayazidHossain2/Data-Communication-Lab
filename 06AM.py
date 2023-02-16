import matplotlib.pyplot as plt 
import numpy as np 


figure, axis = plt.subplots(3)
plt.tight_layout()
#Carrier sigla
step = 0.01
x = list(np.arange(0,5,step))
x.append(x[-1]+step)
A = 5
f = 8
phase = 0
x = np.array(x)

y = A*np.sin(2*np.pi*f*x+phase)

axis[0].grid(True)
axis[0].plot(x,y,color='blue')
axis[0].set_title('Carrier Signal')

#Main Signal
sig_f = 0.5
y1 = (A/3)*((np.sin(2*np.pi*sig_f*x+phase))**3 - (np.cos(2*np.pi*sig_f*x+phase))**2 + (np.cos(2*np.pi*sig_f*x+phase)))
axis[1].grid(True)
axis[1].plot(x,y1,color='green')
axis[1].set_title('Send Signal')

#Modulated Signal
y2 = y + y1
axis[2].grid(True)
axis[2].plot(x,y2,color='red')
axis[2].set_title('Modulated Signal')
plt.show()

# X = np.arange(0, math.pi*2, 0.05)
  
# # Using built-in trigonometric function we can directly plot
# # the given cosine wave for the given angles
# Y1 = np.sin(X)
# Y2 = np.cos(X)
# Y3 = np.tan(X)
# Y4 = np.tanh(X)
  
# # Initialise the subplot function using number of rows and columns
# figure, axis = plt.subplots(4)
  
# # For Sine Function
# axis[0].plot(X, Y1)
# axis[0].set_title("Sine Function")
  
# # For Cosine Function
# axis[1].plot(X, Y2)
# axis[1].set_title("Cosine Function")
  
# # For Tangent Function
# axis[2].plot(X, Y3)
# axis[2].set_title("Tangent Function")
  
# # For Tanh Function
# axis[3].plot(X, Y4)
# axis[3].set_title("Tanh Function")
  
# # Combine all the operations and display
# plt.show()