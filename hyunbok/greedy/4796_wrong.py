a = []
a_l = []
a_p = []
a_v = []
k = 1

while k == 1:
    l, p, v = map(int, input().split())
    if l==0 and p == 0 and v == 0: break
    a_l.append(l)
    a_p.append(p)
    a_v.append(v)

for i in range(len(a_l)):
    l = a_l[i]
    p = a_p[i]
    v = a_p[i]
    temp = 0
    while v>0:
        if v>p:
            v-=p
            temp+=l
        if v<p:
            if v>l:
                temp += l
                v= 0
            if v<l:
                temp +=v
                v = 0
    a.append(temp)

for ans in range(len(a)):
    print('Case ', ans+1, ':', a[ans])



