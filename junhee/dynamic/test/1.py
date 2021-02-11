N = int(input())
square = []
i=1
while True:
    square.append(i**2)
    i += 1
    if square[-1] > N:
        square.pop()
        break
ans = [0 for i in range(N)]
ans.append(-1)

def minsquare(a):
    global ans
    if a < 0 : 
        return N+1
    elif a == 0 :
        return 0
    elif ans[a] != -1:
        return ans[a]
    temp = []
    for i in reversed(range(len(square))):
        temp.append(minsquare(a-square[i]))
    ans[a] = min(temp) + 1
    return ans[a]

print(minsquare(N))