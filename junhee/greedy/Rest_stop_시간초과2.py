L, N, rf, rb = map(int, input().split())
diff = rf-rb
XC=[]
answer = 0
temp = 0

for i in range(N):
    XC.append(list(map(int, input().split())))

XC.sort(key=lambda x : (-x[1],-x[0]))

j = 0
a=0
while True:
    if XC[j][0] > a:
        a = XC[j][0]
        b = XC[j][1]
        answer += (a-temp)*b*(diff)
        temp = a
    while XC[j][1]==b:
        j += 1
        if j == N:
            break
    if j == N:
        break
print(answer)