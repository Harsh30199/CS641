a = ['f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u']
text = []
for x in range(8):
    temp = []
    for i in range(8):
        for j in range(16):
            st = 'ff'*x + a[i]+a[j] + 'ff'*(8-1-x)
            temp.append(st)
    text.append(temp)

file = open('plaintexts.txt','w')
for i in text:
    st = ' '.join(i) + '\n'
    file.write(st)
file.close()

