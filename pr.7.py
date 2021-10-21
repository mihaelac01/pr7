S=str(input('introduceti sirul: '))
print(S)
n=0
for i in S:
    if i=='A':
        n+=1
print('numarul de aparitii a lui "A"= ',n)
Sa=''
for i in S:
    if i=='A':
        Sa+='*'
    else:
        Sa+=i
print('Sirul obtinut prin substituirea caracterului "A" prin caracterul "*"= ',Sa)
Sb=''
for i in S:
    if i!='B':
        Sb+=i
print('sirul obtinut prin radierea caract "B"= ',Sb)
aparitiaMA=0
for i in range(0,len(S)):
    if (S[i]=='M')and(S[i+1]=='A'):
        aparitiaMA+=1
print('numarul de aparitie a silabei "MA"= ',aparitiaMA)
Sc=''
Sm1=S
for i in range(0,len(Sm1)):
    if (S[i]=='M')and(S[i+1]=='A'):
        Sc+='TA'
    else:
        Sc+=S[i]
print('sirul obtinut prin substit silabei "MA" prin silaba "TA"= ',Sc)
Sd=''
Sm2=S
for i in range(0,len(Sm2)):
    if (Sm2[i]=='T')and(Sm2[i+1]=='O'):
        Sd+=Sm2[i]
print('sirul obtinut prin radierea silabei"TO"= ',Sd)
print('sirul inversat= ',S[::-1])






