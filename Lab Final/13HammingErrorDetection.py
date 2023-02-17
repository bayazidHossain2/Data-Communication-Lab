import numpy as np 

inp_signal = input('Enter Hamming Code:')

hammingCode = list()
for i in inp_signal:
    hammingCode.append(ord(i)-48)

print('Hamming code is :',hammingCode)
l = len(inp_signal)
parity_mismatch = list()
for i in range(1,l+1):
    if (np.log2(i)-int(np.log2(i))) == 0.0:
        print(i,'th bit parity calculation')
        parity = 0
        ind = i - 1
        while ind < l:
            for j in range(i):
                if ind >= l:
                    break
                parity = parity + hammingCode[ind]
                print('\t',ind+1,'th bit',hammingCode[ind],'total parity :',parity)
                ind = ind + 1
            for j in range(i):
                if ind >= l:
                    break
                ind = ind + 1
        parity_mismatch.append(parity%2)
        print(i,'th Parity will :',parity_mismatch[-1])

print('-----------Hamming Missmatch Parity code is------------')
print(parity_mismatch)