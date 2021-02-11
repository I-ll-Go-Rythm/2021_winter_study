S=input()
A=int(input())
Dic=[]
for i in range(A):
    Dic.append(input())
Dic.sort(key=lambda x:-len(x)) 
check=0
def isIn(S):
    global Dic
    global check
    c=0
    if(len(S)==0):
        return
    for a in Dic:
        s=S.find(a)
        if(s!=-1):
            isIn(S[0:s])
            isIn(S[s+len(a):])
            c=1
            break
    if(c==0):
        check=1
isIn(S)
if(check==0):
    print('1')
else:
    print('0')