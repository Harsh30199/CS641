#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from pyfinite import ffield
import galois

F = ffield.FField(7, gen=0x83, useLUT=-1)

def Exponentiate(base,power):
    ans = base
    for i in range(1,power):
        ans = F.Multiply(ans,base)
    return ans


def LinearTransform(linmat,msg):
    ans = [0]*8
    for i in range(8):
        temp  = []
        mul = [F.Multiply(linmat[i][j],msg[i]) for j in range(8)]
        for k in range(8):
            temp.append(np.bitwise_xor(ans[k],mul[k]))
        ans = temp
    return ans


# In[2]:


def decode_block(cipher):
  plain= ""
  for i in range(0,len(cipher),2):
      plain+=chr(16*(ord(cipher[i:i+2][0]) - ord('f')) + ord(cipher[i:i+2][1]) - ord('f'))
  return plain


# In[3]:



PossibleExponents = [[] for i in range(8)]   
possibleDiagonalVals=[[[] for i in range(8)] for j in range(8)]
input_file = open('plaintexts.txt','r')
output_file = open('ciphertexts.txt','r')
input = (input_file.readlines()[0]).strip().split(' ')
output = output_file.readlines()

input_string = []
for msg in input:
    input_string.append(decode_block(msg)[0])
#print(input_string)
#print(len(output))
output_string = []
for i in range(len(output)):
    x = []
    for msg in output[i].strip().split(' '):
        x.append(decode_block(msg)[i])
    output_string.append(x)
#print(output_string)
for k in range(8):
    for i in range(1, 127):
        for j in range(1, 128):
          flag = True
          for m in range(128):
            if(ord(output_string[k][m]) != Exponentiate(F.Multiply(Exponentiate(F.Multiply(Exponentiate(ord(input_string[m]), i), j), i), j), i)):
              flag = False
              break
          if(flag):
            PossibleExponents[k].append(i)
            possibleDiagonalVals[k][k].append(j)
print("Possible diagonal values: \n")
print(possibleDiagonalVals)
print("\n\nPossible exponents: \n")
print(PossibleExponents)


output_string = []
for i in range(len(output)-1):
    x = []
    for msg in output[i].strip().split(' '):
        x.append(decode_block(msg)[i+1])
    output_string.append(x)

for ind in range(7):
  for i in range(1, 128):
      for p1, e1 in zip(PossibleExponents[ind+1], possibleDiagonalVals[ind+1][ind+1]):
          for p2, e2 in zip(PossibleExponents[ind], possibleDiagonalVals[ind][ind]):
              for k in range(128):
                  flag = True
                  x1 = F.Multiply(Exponentiate(F.Multiply(Exponentiate(ord(input_string[k]), p2), e2), p2), i)
                  x2 = F.Multiply(Exponentiate(F.Multiply(Exponentiate(ord(input_string[k]), p2), i), p1), e1)
                  c1 = np.bitwise_xor(x1,x2)
                  if(ord(output_string[ind][k]) != Exponentiate(c1,p1)):
                      flag = False
                      break
              if flag:
                  PossibleExponents[ind+1] = [p1]
                  possibleDiagonalVals[ind+1][ind+1] = [e1]
                  PossibleExponents[ind] = [p2]
                  possibleDiagonalVals[ind][ind] = [e2]
                  possibleDiagonalVals[ind][ind+1] = [i]
print('\n\n===========================\n\n')
print("Linear Transformation Matrix A values: \n")
print(possibleDiagonalVals)
print("\n\nExponent Vector E values : \n")
print(PossibleExponents)


# In[4]:


def EAEAE (msg, lin_mat, exp_mat):
  msg = [ord(m) for m in msg]
  res = [Exponentiate(msg[i], exp_mat[i]) for i in range(8)]
  res = LinearTransform(lin_mat, res)
  res = [Exponentiate(res[i], exp_mat[i]) for i in range(8)]
  res = LinearTransform(lin_mat, res)
  res = [Exponentiate(res[i], exp_mat[i]) for i in range(8)]
  return res


input_file = open('plaintexts.txt','r')
output_file = open('ciphertexts.txt','r')
input = input_file.readlines()
output = output_file.readlines()


input_string = []
for i in range(len(input)):
    x = []
    for msg in input[i].strip().split(' '):
        x.append(decode_block(msg))
    input_string.append(x)


output_string = []
for i in range(len(output)):
    x = []
    for msg in output[i].strip().split(' '):
        x.append(decode_block(msg))
    output_string.append(x)

for indexex in range(0,6):
    offset = indexex + 2
    
    exp_list = [e[0] for e in PossibleExponents]
    lin_trans_list = np.zeros((8,8),int)

    for i in range(8):
      for j in range(8):     
        if(len(possibleDiagonalVals[i][j]) != 0):
            lin_trans_list[i][j] = possibleDiagonalVals[i][j][0]
        else:
            lin_trans_list[i][j] = 0
    
    for index in range(8):
        if(index > (7-offset)):
            continue

        for i in range(127):
            lin_trans_list[index][index+offset] = i+1
            flag = True
            for inps, outs in zip(input_string[index], output_string[index]):
                x1 = EAEAE(inps, lin_trans_list, exp_list)[index+offset]
                x2 = outs[index+offset]
                if x1 != ord(x2):
                    flag = False
                    break
            if flag==True:
                possibleDiagonalVals[index][index+offset] = [i+1]
                
A = np.zeros((8,8),dtype='int')

for i in range(0,8):
    for j in range(0,8):
      if len(possibleDiagonalVals[j][i]) != 0:
       A[i][j] = possibleDiagonalVals[j][i][0]



E = exp_list

print('\n\nLinear Transformation Matrix :\n',A)
print('\n\n')
print('Exponent Vector : \n',E)


# In[5]:


Einverse = np.zeros((128, 128), dtype = int)

for base in range(0,128):
    temp = 1
    for power in range(1,127):
        result = F.Multiply(temp, base)
        Einverse[power][result] = base
        temp = result
    
GF = galois.GF(2**7)
A = GF(A)
invA = np.linalg.inv(A)


# In[6]:


password = "gsfojqmrimffismjfkjtkpkujlmjhjkp" #Encrypted password
GF = galois.GF(2**7)

def Einv(block, E):
    return [Einverse[E[i]][block[i]] for i in range(8) ]

def Ainv(block, A):
    block = GF(block)
    A = GF(A)
    return np.matmul(A,block)

decrypted_password = ""
for i in range(0,2): 
    elements = password[16*i:16*(i+1)]
    currentBlock = []
    for j in range(0,15,2):
        currentBlock+=[(ord(elements[j]) - ord('f'))*16 + (ord(elements[j+1]) - ord('f'))]
    EAEAE = Einv(Ainv(Einv(Ainv(Einv(currentBlock, E), invA),E), invA),E)
    for ch in EAEAE:
        decrypted_password += chr(ch)
    
print("\n\nPassword is",decrypted_password)
    

