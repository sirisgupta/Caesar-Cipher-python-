def cce(au,sk):
    a=au.upper()
    l1=[]
    li="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in a:
        ctr=0
        for j in li:
            if i==j:
                l1.append(li[ctr+sk])
            ctr+=1

    print(l1)
    x=''.join(l1)
    print(x)

cce("siris",4)
