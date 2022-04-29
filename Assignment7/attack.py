from itertools import combinations_with_replacement
from random import choices

num = [24,69, 53, 32, 23, 40, 36, 117, 20, 16, 65, 121, 96, 113, 27, 43, 83, 80, 44, 110, 105, 17, 77, 26, 23, 91, 48, 115, 2, 42, 74, 122]

a = list(combinations_with_replacement(range(102,118),6))

while(True):
  sample = choices(a,k=4)
  inp = []
  count = 0
  for i in range(4):
    inp+= sample[i]

  for i in range(1,32):
    sum1 = sum([x**i for x in inp])%127
    if(sum1 != num[i]):
      break
    count+=1

  if(count==31):
    l = inp
    break

##l = [102, 104, 106, 108, 109, 109, 104, 107, 111, 113, 113, 116, 102, 105, 109, 111, 113, 117, 105, 106, 106, 108, 112, 113]

l = sorted(l)

for i  in l:
    print(chr(i),end='')
