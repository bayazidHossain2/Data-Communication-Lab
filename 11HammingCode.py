import numpy as np

while(True):
    inp_signal = input('Enter Message signal : ')

    m = len(inp_signal)
    r = int(np.log2(m))

    while(2**r < m+r+1):
        r = r + 1

    l = m+r
    print('-> Message len : ',m ,' -> Redundant len : ',r, ' -> Total len : ',l)

    hammingCode = list()
    str_ind = 0
    # Inserting the message signal to the list.
    for i in range(1,l+1):
        
        if (np.log2(i)-int(np.log2(i))) == 0.0:
            hammingCode.append(0)
            print(i,'is a power of 2.')
        else :
            hammingCode.append(int(ord(inp_signal[str_ind])-48))
            str_ind = str_ind + 1
    print('Mid Message is : ',hammingCode)
    # Inserting the Redundant bit to the list.
    for i in range(1,l+1):
        if (np.log2(i)-int(np.log2(i))) == 0.0:
            print(i,'is a power of 2.')
            parity = 0
            ind = i-1
            while(ind < l):
                for j in range(i):
                    if ind >= l:
                        break
                    parity = parity + hammingCode[ind]
                    print(ind+1, hammingCode[ind],'th parity is added : ',parity)
                    ind = ind + 1
                for j in range(i):
                    if ind >= l:
                        break
                    ind = ind + 1
            hammingCode[i-1] = (parity%2)
            print(i,'Redundant parity is : ',parity,' hamming : ',hammingCode[i-1])                

    print('--------Hamming code is --------')
    print(hammingCode)

