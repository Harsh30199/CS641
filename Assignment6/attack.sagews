︠30b24939-159e-4c96-bd55-0810b78ea9ecs︠
# This worksheet was converted from a notebook running Jupyter kernel
# version sage-9.5.
︡e8c1aedc-ad97-4cb3-8fc4-27bfea552b58︡{"done":true}
︠466dd913-01c3-43dc-aa8c-a8e766dad33fso︠
N=84364443735725034864402554533826279174703893439763343343863260342756678609216895093779263028809246505955647572176682669445270008816481771701417554768871285020442403001649254405058303439906229201909599348669565697534331652019516409514800265887388539283381053937433496994442146419682027649079704982600857517093

C=17682209225809987046236362123205092817571021518027707375108020700729482152654000137158934080739905216856837090607144440344031927906581569868080227308437728529982122166164583798842879622125932314538073945937211188090137025280486461868383287642100592253980842953009393121691419057911851803717308465337876292661

e=5

msg = "Lazarus: This door has RSA encryption with exponent 5 and the password is "

Zn = Zmod(N)
maxpasslen = 200

msgbin = ''
for i in msg:
    t = str(bin(ord(i))[2:])
    msgbin += ('0'*(8-len(t)) + t)

msgint = int(msgbin,2)

for l in range(0, maxpasslen+1, 4):

    P.<M> = PolynomialRing(Zn)
    pol = ((msgint<<l) + M)^e - C
    d = pol.degree()
    m = ceil((d * (1/7))**-1)
    ## With our choice of beta parameter t is eliminated as it is always 0
    X = ceil(N**((1/d) - (1/7)))

    polz = pol.change_ring(ZZ)
    x = polz.parent().gen()


    pols = [] # Polynomials
    for i in range(m):
        for j in range(d):
            pols+=[pow((x * X),j) * pow(N,(m - i)) * pow(polz(x * X),i)]


    n = d * m
    B = Matrix(ZZ, n) # Lattice B

    for i in range(n):
        B[i] = list(pols[i])[0:i+1]+ [0]*(n-i-1)

    B = B.LLL() # LLL

    new_pol = 0
    for i in range(n):
        new_pol = new_pol + pow(x,i) * B[0, i] / pow(X,i) # shortest vector

    posroots = new_pol.roots() # Stores the possible roots

    roots = [] # true roots
    for root in posroots:
        root = root[0]
        if root == round(root,0):
            result = polz(ZZ(root))
            if gcd(N, result) == N:
                roots=ZZ(root)
    if roots:
        r = bin(roots)[2:]
        print("The correct root is :", r)


        print(len(r))

        r = '0'*(l-len(r))+r
        print('Correct root with length divisible by 8 is :',r)
        password = ''
        for i in range(0,len(r)-7,8):

            password+=str(chr(int(r[i:i+8],2)))

        print('Password is',password)
        break
︡a66ce750-cecc-4ac6-bcf3-80e417727a1c︡{"stdout":"The correct root is :"}︡{"stdout":" 1000011001110000101100101010000001101110110111101001100011011110011011001011001\n79\nCorrect root with length divisible by 8 is : 01000011001110000101100101010000001101110110111101001100011011110011011001011001\nPassword is C8YP7oLo6Y\n"}︡{"done":true}









