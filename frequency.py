a = 'DF ULYP XO CQD LFWC RUBHEDY, CQDYG LN XDYL EGIYIG LMP CQDYF. LYFNH HXPZ CQF YNILXKPB "NDCB_AN_BBHCN" PQ FQ CQPKZBK. OLC PMCUNUG YMB IPYDIDCQ OXY CMB LDZP AULHDFY. CX OALG RMB FWGI PMXBNTIP ZLSWS LFWFE PQ ZCYGY KIBAT XMNKI PMBYD.'

a = a.lower()

count = {}

for i in a:

    if i in count.keys():

        count[i] = count[i] + 1

    else:

        count[i] = 1



IC = 0;

total_count = 0;

for i in count.keys():

    if i.isalpha():

        IC = IC + count[i]*(count[i]-1)

        total_count = total_count + count[i]



IC = IC/(total_count*(total_count-1))

print(count)

print(IC)
