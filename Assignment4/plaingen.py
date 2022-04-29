#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random

hex2char = {
 '0000': 'd',
 '0001': 'e',
 '0010': 'f',
 '0011': 'g',
 '0100': 'h',
 '0101': 'i',
 '0110': 'j',
 '0111': 'k',
 '1000': 'l',
 '1001': 'm',
 '1010': 'n',
 '1011': 'o',
 '1100': 'p',
 '1101': 'q',
 '1110': 'r',
 '1111': 's'
}

char2hex = {x:y for y,x in hex2char.items()}
# characteristic is 40 08 00 00 04 00 00 00
# XOR value between pairs of plaintexts is 0x0000801000004000
XOR_value = list((bin(0x0000801000004000))[2:].zfill(64))
XOR_value = [int(x) for x in XOR_value]
binplaintexts = []
for i in range(5000):
    tmp = np.random.choice(['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'],size=(1,16),replace = True)[0]
    bininput=[]
    for i in tmp:
        bininput.extend([int(a) for a in char2hex[i]])

    binplaintexts.append(bininput)
    binplaintexts.append(list(np.bitwise_xor(bininput,XOR_value)))

plaintexts = []

for i in range(len(binplaintexts)):
    s = ""
    for j in range(0,64,4):

        s+=hex2char[''.join([str(a) for a in binplaintexts[i][j:j+4]])]

    plaintexts+=[s]

file = open("plaintexts1.txt","w")
for plaintext in plaintexts:
    file.write(plaintext+"\n")
file.close()


# In[2]:

#charateristic is 00 20 00 08 00 00 04 00
# XOR value between pairs of plaintexts is  0x0000080100100000
XOR_value = list((bin(0x0000080100100000))[2:].zfill(64))
XOR_value = [int(x) for x in XOR_value]
binplaintexts = []
for i in range(5000):
    tmp = np.random.choice(['d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s'],size=(1,16),replace = True)[0]
    bininput=[]
    for i in tmp:
        bininput.extend([int(a) for a in char2hex[i]])

    binplaintexts.append(bininput)
    binplaintexts.append(list(np.bitwise_xor(bininput,XOR_value)))

plaintexts = []

for i in range(len(binplaintexts)):
    s = ""
    for j in range(0,64,4):

        s+=hex2char[''.join([str(a) for a in binplaintexts[i][j:j+4]])]
    plaintexts+=[s]

file = open("plaintexts2.txt","w")
for plaintext in plaintexts:
    file.write(plaintext+"\n")
file.close()

