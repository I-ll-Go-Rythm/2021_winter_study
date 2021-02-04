N = int(input())
homework =[]
available =[]
temp = 0
answer = 0
for i in range(N):
    homework.append(list(map(int,input().split())))
homework.sort(reverse=True)

i=0

j = homework[0][0]
while j > 0:
    if i != N:
        while homework[i][0] == j:
            i += 1
            if i == N:
                break
        available += list(map(lambda x : x[1], homework[temp:i]))
        temp = i
    if len(available)!=0:
        answer += max(available)
        available.remove(max(available))
    j -= 1
print(answer)

#밑에는 뻘짓한 흔적...ㅠ
""" i = 0
while i < N:
    while homework[i][0] == days and temp < days:
        filt.append(homework[i])
        temp += 1
        i += 1
        if i == N:
            break
    if i == N:
        break
    while homework[i][0] == days:
        i += 1
        if i == N:
            break
    if i == N:
        break
    days = homework[i][0]
    temp = 0 """