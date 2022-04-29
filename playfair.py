import numpy as np
cipher = 'DF ULYP XO CQD LFWC RUBHEDY, CQDYG LN XDYL EGIYIG LMP CQDYF. LYFNH HXPZ CQF YNILXKPB "NDCB_AN_BBHCN" PQ FQ CQPKZBK. OLC PMCUNUG YMB IPYDIDCQ OXY CMB LDZP AULHDFY. CX OALG RMB FWGI PMXBNTIP ZLSWS LFWFE PQ ZCYGY KIBAT XMNKI PMBYD.'

cipher2= ''

for c in cipher:
    if ord(c) in range(65,91):
        cipher2+=c

playmat=[]
added = []
key = 'CRYPTANALYSIS'

for s in key:
    if s not in added:
        playmat.append(s  if s not in ['j','J'] else 'I')
        added.append(s)

for i in range(65,91):
    if chr(i) not in added and chr(i)!='J':
        playmat.append(chr(i))
        added.append(chr(i))


playmat = np.array(playmat).reshape(5,5)

print(playmat)


plain = ''
l1 = l2 = l3 =[]
for i in range(0,len(cipher2)-1,2):
    x1,y1 = np.where(playmat == cipher2[i])
    x2,y2 = np.where(playmat == cipher2[i+1])
    x1 = x1[0]
    x2 = x2[0]
    y1 = y1[0]
    y2 = y2[0]
    
    if y1 == y2:
        a = playmat[x1-1][y1] if x1>0 else playmat[4][y1]
        b = playmat[x2-1][y1] if x2>0 else playmat[4][y1]
        plain+=(a+b)
        l1.append([cipher2[i],cipher2[i+1],a,b])

    elif x1 == x2:
        a = playmat[x1][y1-1] if y1>0 else playmat[x1][4]
        b = playmat[x1][y2-1] if y2>0 else playmat[x1][4]
        plain+=(a+b)
        l2.append([cipher2[i],cipher2[i+1],a,b])
    else:
        plain+=playmat[x1][y2]
        plain+=playmat[x2][y1]
        l3.append([cipher2[i],cipher2[i+1],a,b])
        
    
print('\n\n',plain)
               
print(l1,l2,l3)
