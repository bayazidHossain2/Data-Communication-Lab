import numpy as np

while(True):
    inp_signal = input('Enter Message signal : ')

    hammingCode = list()
    for i in range(len(inp_signal)):
        hammingCode.append(ord(inp_signal[i])-48)

    parity_mismatch = list()
    for i in range(1,len(inp_signal)+1):
        if (np.log2(i)-int(np.log2(i))) == 0.0:
            print(i,'is a power of 2.')
            parity = 0
            ind = i-1
            while(ind < len(hammingCode)):
                for j in range(i):
                    if ind >= len(hammingCode):
                        break
                    parity = parity + hammingCode[ind]
                    print(ind+1, hammingCode[ind],'th parity is added : ',parity)
                    ind = ind + 1
                for j in range(i):
                    if ind >= len(hammingCode):
                        break
                    ind = ind + 1
            parity_mismatch.append(parity%2)
            print(i,'Redundant parity is : ',parity,' hamming : ',parity_mismatch[-1])                

    print('--------Missmatch code is --------')
    print(parity_mismatch)

