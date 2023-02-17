import numpy as np
inp_signal = input('Enter Message Signal : ')
m = len(inp_signal)
r = int(np.log2(m))
while(2**r < m+r+1):
    r = r + 1
l = m+r 
print('-> Message len :',m,' -> Redundant len :',r,' -> Total len :',l)
hammingCode = list()
sig_ind = 0
for i in range(1,l+1):
    if (np.log2(i)-int(np.log2(i)) == 0.0):
        hammingCode.append(0)
    else:
        hammingCode.append(ord(inp_signal[sig_ind])-48)
        sig_ind = sig_ind + 1
print('Before Calculating Redundant Bit : ',hammingCode)
for i in range(1,l+1):
    if (np.log2(i)-int(np.log2(i)) == 0.0):
        print('\t',i,'th bit parity calculation')
        parity = 0
        ind = i - 1
        while ind < l:
            for j in range(i):
                if ind >= l:
                    break
                parity = parity + hammingCode[ind]
                print('\t\t',ind+1,'th bit',hammingCode[ind],'total parity :',parity)
                ind = ind + 1
            for j in range(i):
                if ind >= l:
                    break
                ind = ind + 1
        hammingCode[i-1] = parity%2
        print('\t',i,'th Parity will :',hammingCode[i-1])
print('-----------Generated Hamming code is------------')
print(hammingCode)

