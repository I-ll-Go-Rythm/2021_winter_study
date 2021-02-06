def max_box(A): #A를 이용해 박스를 채울 수 있는 최대 개수
    global length, width, height
    return (length//A)*(width//A)*(height//A)

length, width, height = map(int, input().split())
N = int(input())
cube = [], answer = 0, temp = 0, tempsum = 0
for i in range(N):
    Ai, Bi = map(int, input().split())
    cube.append([2**Ai,Bi])

cube.sort(reverse=True)

for i in range(N):
    if max_box(cube[i][0]) == 0:
        continue
    mx = max_box(cube[i][0])-tempsum
    cunum = cube[i][1]
    if cunum >= mx:
        temp = mx
    else:
        temp = cunum
    answer += temp
    tempsum *= 8
    tempsum += temp*8
    if i == N-1 :
        if temp != mx:
            print(-1)
        else:
            print(answer)