#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


# Permute function to rearrange the bits 
def permute(k, arr, n): 
    permutation = "" 
    for i in range(0, n): 
        permutation = permutation + k[arr[i] - 1] 
    return permutation 
  
# shifting the bits towards left by nth shifts 
def shift(k, n): 
    return k[n:] + k[0:n]


# In[3]:


# Expansion E-box Table 
E = [32, 1 , 2 , 3 , 4 , 5 , 4 , 5,  
         6 , 7 , 8 , 9 , 8 , 9 , 10, 11,  
         12, 13, 12, 13, 14, 15, 16, 17,  
         16, 17, 18, 19, 20, 21, 20, 21,  
         22, 23, 24, 25, 24, 25, 26, 27,  
         28, 29, 28, 29, 30, 31, 32, 1 ] 
  
#Inverse of P
INVP = [9, 17, 23, 31,
	      13, 28,  2, 18,
	      24, 16, 30,  6,
	      26, 20, 10,  1,
	       8, 14, 25,  3,
	       4, 29, 11, 19,
	      32, 12, 22,  7,
	       5, 27, 15, 21
        ]

# S-box Table 
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3 , 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1 , 14, 8, 13, 6, 2, 11, 15, 12, 9, 7,3, 10, 5, 0],
    [15, 12, 8,2,4, 9, 1,7 , 5, 11, 3, 14, 10, 0, 6, 13]],

    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0,5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8,12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2,11,6, 7, 12, 0,5, 14, 9]],

    [[10, 0, 9,14,6,3,15,5, 1, 13, 12, 7, 11, 4,2,8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12,5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1 , 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11,2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

    [[12, 1, 10, 15, 9, 2, 6,8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2,8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12,7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]] 
    



f2u_mapping={'d': '0000',
             'e': '0001',
             'f': '0010',
             'g': '0011',
             'h': '0100',
             'i': '0101',
             'j': '0110',
             'k': '0111',
             'l': '1000',
             'm': '1001',
             'n': '1010',
             'o': '1011',
             'p': '1100',
             'q': '1101',
             'r': '1110',
             's': '1111'}
     
## Key Schedule
PC2 = [                 
  14, 17, 11, 24,  1, 5, 
  3, 28 ,15,  6, 21, 10, 
  23, 19, 12,  4, 26, 8, 
  16,  7, 27, 20, 13, 2, 
  41, 52, 31, 37, 47, 55, 
  30, 40, 51, 45, 33, 48, 
  44, 49, 39, 56, 34, 53, 
  46, 42, 50, 36, 29, 32
]

## Reverse Final Permutation
RFP = [57, 49, 41, 33, 25, 17, 9,  1,
       59, 51, 43, 35, 27, 19, 11, 3,
       61, 53, 45, 37, 29, 21, 13, 5,
       63, 55, 47, 39, 31, 23, 15, 7,
       58, 50, 42, 34, 26, 18, 10, 2,
       60, 52, 44, 36, 28, 20, 12, 4,
       62, 54, 46, 38, 30, 22, 14, 6,
       64, 56, 48, 40, 32, 24, 16, 8]

#shift table 
shift_table = [1, 1, 2, 2,  
                2, 2, 2, 2,  
                1, 2, 2, 2,  
                2, 2, 2, 1 ] 
  
# Key- Compression Table : Compression of key from 56 bits to 48 bits 
key_comp = [14, 17, 11, 24, 1, 5,  
            3, 28, 15, 6, 21, 10,  
            23, 19, 12, 4, 26, 8,  
            16, 7, 27, 20, 13, 2,  
            41, 52, 31, 37, 47, 55,  
            30, 40, 51, 45, 33, 48,  
            44, 49, 39, 56, 34, 53,  
            46, 42, 50, 36, 29, 32 ] 
  

mapping = {
           'd' : [0,0,0,0],
           'e' : [0,0,0,1],
           'f' : [0,0,1,0],
           'g' : [0,0,1,1],
           'h' : [0,1,0,0],
           'i' : [0,1,0,1],
           'j' : [0,1,1,0],
           'k' : [0,1,1,1],
           'l' : [1,0,0,0],
           'm' : [1,0,0,1],
           'n' : [1,0,1,0],
           'o' : [1,0,1,1],
           'p' : [1,1,0,0],
           'q' : [1,1,0,1],
           'r' : [1,1,1,0],
           's' : [1,1,1,1]
          }

# Permutation at start of DES
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,  
                60, 52, 44, 36, 28, 20, 12, 4,  
                62, 54, 46, 38, 30, 22, 14, 6,  
                64, 56, 48, 40, 32, 24, 16, 8,  
                57, 49, 41, 33, 25, 17, 9, 1,  
                59, 51, 43, 35, 27, 19, 11, 3,  
                61, 53, 45, 37, 29, 21, 13, 5,  
                63, 55, 47, 39, 31, 23, 15, 7]

## S Box Permutation Table
sboxper = [ 16,  7, 20, 21, 
        29, 12, 28, 17,  
         1, 15, 23, 26,  
         5, 18, 31, 10,  
         2,  8, 24, 14,  
        32, 27,  3,  9,  
        19, 13, 30,  6,  
        22, 11,  4, 25 ] 
        
## Permutation at the end of DES
final_perm = [ 40, 8, 48, 16, 56, 24, 64, 32,  
               39, 7, 47, 15, 55, 23, 63, 31,  
               38, 6, 46, 14, 54, 22, 62, 30,  
               37, 5, 45, 13, 53, 21, 61, 29,  
               36, 4, 44, 12, 52, 20, 60, 28,  
               35, 3, 43, 11, 51, 19, 59, 27,  
               34, 2, 42, 10, 50, 18, 58, 26,  
               33, 1, 41, 9, 49, 17, 57, 25 ] 


# In[4]:


#Computing XORs at IN and OUT of S-boxes for characteristic 40 08 00 00 04 00 00 00


ciphertext = open('ciphertexts1.txt').read().split("\n")

hexcipher =[]
for c in ciphertext:
  h=[]
  if len(c) == 16:
    for i in range(16):
      h.extend(mapping[c[i]])
    hexcipher.extend([h])


##Inverse the final permutation

invres = []
for c in hexcipher:
  temp=[]
  for i in range(64):
    temp.extend([c[RFP[i]-1]])

  invres.extend([temp])


##Xoring the ciphertext pairs according to differential

resxor = []
for i in range(0,len(invres)//2):
  resxor.extend([list(np.bitwise_xor(invres[2*i],invres[2*i+1]))])

##Expanding Right side block of Round 5

expanded = []

for i in range(0,len(invres)):
  temp = []
  for j in range(48):
    temp.extend([invres[i][E[j]-1]])

  expanded.extend([temp])

##Xoring expanded to compute s box input

sin = []
for i in range(0,len(expanded)//2):
  sin.extend([list(np.bitwise_xor(expanded[2*i],expanded[2*i+1]))])

##Xoring L5 and R6

L5 = [0,0,0,0,0,1]+[0]*26
inxor = []
for i in resxor:
  inxor.extend([list(np.bitwise_xor(i[32:64],L5))])

##Xoring sbox outputs

sxor =[]
for i in inxor:
  temp = []
  for j in range(32):
    temp.extend([i[INVP[j]-1]])
  sxor.extend([temp])

##Finding the Keys  corresponding to Round 6 for above charcateristic

keys = np.zeros((8,64))

for i in range(len(sin)):
  if sin[i]=="":
        continue 
  for j in range(0,8):
    inx = int(''.join([str(s) for s in sin[i][j*6:j*6+6]]),2)
    outx = int(''.join([str(s) for s in sxor[i][j*4:j*4+4]]),2)
    inp = int(''.join([str(s) for s in expanded[2*i+1][j*6:j*6+6]]),2)
 
    for k in range(0,64):
      a = bin(k)[2:].zfill(6)
      b = bin(k^inx)[2:].zfill(6)
      if outx == sbox[j][int(a[0])*2 + int(a[5])][int(a[4]) + 2 *int(a[3]) + int(a[2]) * 4 + int(a[1])*8]^sbox[j][int(b[0])*2 + int(b[5])][int(b[4]) + 2 *int(b[3]) + int(b[2]) * 4 + int(b[1])*8]:
        keys[j][k^inp]+=1
  
 
print(keys)


# In[5]:


maxval = [] 
mean = [] 
keyval = [] 
for i in range(len(keys)):     
  mean.append(int(keys[i].mean()))     
  current = max(keys[i])     
  maxval.append(current)     
  keyval.append(np.where(keys[i]==current)[0][0]) 

print("S-box"+ "\t" +"Max" + "\t" + "Mean" + "\t" + "Key") 
for i in range(0,8):     
  print("S"+ str(i+1) +"\t"+ str(maxval[i]) + "\t" + str(mean[i]) + "\t" + str(keyval[i]))


# In[6]:


#Computing XORs at IN and OUT of S-boxes for characteristic 40 08 00 00 04 00 00 00


ciphertext = open('ciphertexts2.txt').read().split("\n")

hexcipher =[]
for c in ciphertext:
  h=[]
  if len(c) == 16:
    for i in range(16):
      h.extend(mapping[c[i]])
    hexcipher.extend([h])

##Inverse the final permutation

invres = []
for c in hexcipher:
  temp=[]
  for i in range(64):
    temp.extend([c[RFP[i]-1]])
  invres.extend([temp])


##Xoring the ciphertext pairs according to differential

resxor = []
for i in range(0,len(invres)-1,2):
  resxor.extend([list(np.bitwise_xor(invres[i],invres[i+1]))])


##Expanding Right side block of Round 5

expanded = []

for i in invres:
  temp = []
  for j in range(48):
    temp.extend([i[E[j]-1]])
  expanded.extend([temp])

##Xoring expanded to compute s box input

sin = []
for i in range(0,len(expanded)-1,2):
  sin.extend([list(np.bitwise_xor(expanded[i],expanded[i+1]))])

##Xoring L5 and R6

L5 = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]
inxor = []
for i in resxor:
  inxor.extend([list(np.bitwise_xor(i[32:64],L5))])

##Xoring sbox outputs

sxor =[]
for i in inxor:
  temp = []
  for j in range(32):
    temp.extend([i[INVP[j]-1]])
  sxor.extend([temp])

##Finding the Keys  corresponding to Round 6 for above charcateristic

keys = np.zeros((8,64))

for i in range(len(sin)):
  for j in range(0,8):
    inx = int(''.join([str(s) for s in sin[i][j*6:j*6+6]]),2)
    outx = int(''.join([str(s) for s in sxor[i][j*4:j*4+4]]),2)
    inp = int(''.join([str(s) for s in expanded[2*i+1][j*6:j*6+6]]),2)

    for k in range(0,64):
      a = bin(k)[2:].zfill(6)
      b = bin(k^inx)[2:].zfill(6)
      if outx == sbox[j][int(a[0])*2 + int(a[5])][int(a[4]) + 2 *int(a[3]) + int(a[2]) * 4 + int(a[1])*8]^sbox[j][int(b[0])*2 + int(b[5])][int(b[4]) + 2 *int(b[3]) + int(b[2]) * 4 + int(b[1])*8]:
        keys[j][k^inp]+=1
 
print(keys)


# In[7]:


maxval = [] 
mean = [] 
keyval = [] 
for i in range(len(keys)):     
  mean.append(int(keys[i].mean()))     
  current = max(keys[i])     
  maxval.append(current)     
  keyval.append(np.where(keys[i]==current)[0][0]) 

print("S-box"+ "\t" +"Max" + "\t" + "Mean" + "\t" + "Key") 
for i in range(0,8):     
  print("S"+ str(i+1) +"\t"+ str(maxval[i]) + "\t" + str(mean[i]) + "\t" + str(keyval[i]))


# In[8]:


## Finding the Key

sbkey = "101101111011XXXXXX000111000110011111000000110010" ##Obtained by converting key value to binary for each sbox 1 to 8 except 3 for which 'XXXXXX' is appended as input to sbox 3 is never 0

key = ['X']*56

for i in range(48):
  key[PC2[i]-1] = sbkey[i]

for i in range(0,6):
  for j in range(shift_table[i]):
    x = key[27]
    y = key[55]

    for k in range(27,0,-1):
      key[k] = key[k-1]
      key[k+28] = key[k+27]

    key[0] = x
    key[28] = y

print(''.join(key))
miskey = ''.join(key)


# Using Brute Force Method to find mising 14 bits of key

# In[9]:



poskey = []
binlist = []
for i in range(2**14):
  x = str(bin(i)[2:])
  binlist.append(('0')*(14-len(x))+x)

for i in binlist:
  j = 0
  tempkey = list(miskey)
  for k in range(len(tempkey)):
    if tempkey[k] == 'X':
      tempkey[k] = i[j]
      j+=1
  poskey.append(''.join(tempkey))



def roundkey(k,rno):
  left = k[0:28]
  right = k[28:56]

  binkey = []

  for i in range(rno):
    left = shift(left,shift_table[i])
    right = shift(right,shift_table[i])

    key = left + right

    binkey.extend([permute(key,key_comp,48)])

  return binkey


def encryption(mess,key,rno):

  mess = permute(mess,initial_perm,64)

  left = mess[:32]
  right = mess[32:]

  for i in range(rno):
   ## print(i)
    ##if(i==4):
      ##print(right,left)
    expmess = permute(right,E,48)
   ## print(int(expmess,2),int(key[i],2))
    inxor = str(bin(np.bitwise_xor(int(expmess,2),int(key[i],2)))[2:])
    if(len(inxor)!=48):
      inxor= ('0'*(48-len(inxor)))+inxor
    ##print(inxor,len(inxor))
    ##Computing Sbox output for inxor
    sout = ''
    for j in range(8):
      temp = (bin(sbox[j][int(inxor[j*6]+inxor[j*6+5],2)][int(inxor[j*6+1:j*6+5],2)])[2:])
      sout+= ('0'*(4-len(temp))+temp)
    sout = permute(sout,sboxper,32)

    roundxor = str(bin(np.bitwise_xor(int(left,2),int(sout,2)))[2:])
    # if(i==3):
    #   print(roundxor,len(roundxor))
    if(len(roundxor)!=32):
      roundxor= ('0'*(32-len(roundxor)))+roundxor
    left = roundxor

    if(i!=5):
      t = left
      left = right
      right = t

    
  outmess = left + right
  cipher = permute(outmess,final_perm,64)

  return cipher


# In[10]:


mainkey = ''
binplain = ''
for i in 'defghijklmnopqrs':
  binplain+= f2u_mapping[i]

bincipher = ''
for i in "qpnonsgrprdllqml":
  bincipher+=f2u_mapping[i]

for k in poskey:
  key = roundkey(k,6)
  if(encryption(binplain,key,6)== bincipher):
    mainkey = k
    print('The key is',k,'\n')
    for i in range(6):
      print('Round',i,'key is',key[i])
    
    break


# In[11]:


## seperate key into comma seperated

for i in mainkey:
    print(i+',',end='')


# In[12]:


## Convert main cipher text to decimal values

password = 'leohimkjkshooerdqqngsgmnjjmjpfdm'

for i in range(0,len(password),2):
    a = f2u_mapping[password[i]]+f2u_mapping[password[i+1]]
    b = int(a,2)
    print(password[i:i+2],b)

