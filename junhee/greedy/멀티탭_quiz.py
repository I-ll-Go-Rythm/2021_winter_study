N,K = map(int,input().split())
elec = list(map(int,input().split()))
plug = []
answer = 0
for i in range(N):
    plug.append(0)

for E in range(K):
    if elec[E] in plug:
        continue
    for i in range(N):
        if plug[i] == 0 :
            plug[i] = elec[E]
            break
    else:
        repeat = []
        for i in range(N):
            if plug[i] in elec[E+1:]:
                repeat.append(E+1+elec[E+1:].index(plug[i]))
            else:
                plug[i] = elec[E]
                answer += 1
                break
        if len(repeat) == N :
            a = elec[max(repeat)]
            plug[plug.index(a)] = elec[E]
            answer += 1
print(answer)