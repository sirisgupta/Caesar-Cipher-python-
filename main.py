#code for caesar cipher encrypt
def cce(au,sk):
    a=au.upper()
    l1=[]
    li="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    for i in a:
        ctr=0
        if i==" ":
                l1.append(" ")
        for j in li:
            if i==j:
                l1.append(li[ctr+sk])
            
            ctr+=1
    x=''.join(l1)
    print(x) 




#code for caesar cipher decrypt

def ccd(au,sk):
    a=au.upper()
    l1=[]
    li="ZYXWVUTSRQPONMLKJIHGFEDCBA"
    
    for i in a:
        ctr=0
        if i==" ":
                l1.append(" ")
        for j in li:
            if i==j:
                l1.append(li[ctr+sk])
            
            ctr+=1
    x=''.join(l1)
    print(x) 



#word encrypter
word=input("Enter word : ")
ch=input("Do you want to encrypt or decrypt using Caesar Cipher ? E/D :")

cho=ch.upper()
b=int(input("Provide shift key :"))
    
if cho=="E":
    #call encrypt function here
    cce(word,b)
elif cho=="D":
    #call decrypt function here
    ccd(word,b)
else:
    print("Invalid input, program shutting down.")








    



