def max_box(A): #큐브 A를 이용해 박스를 채울 수 있는 최대 개수
    global length, width, height
    return (length//A)*(width//A)*(height//A)

length, width, height = map(int, input().split())
N = int(input()) #큐브 종류의 개수
cube = [] 
answer = 0
temp = 0
tempsum = 0

for i in range(N):
    Ai, Bi = map(int, input().split())
    cube.append([2**Ai,Bi])

cube.sort(reverse=True)#큐브를 크기 순으로 오름차순 정렬

for i in range(N):
    if max_box(cube[i][0]) == 0: #애초에 못채우니 continue
        continue
    mx = max_box(cube[i][0])-tempsum #i번째 큐브로 채울 수 있는 실제 개수(앞서 채워진 큐브들이 있는 상황까지 고려한 값) 
    cunum = cube[i][1] #i번째 큐브의 개수
    if cunum >= mx:
        temp = mx
    else:
        temp = cunum
    answer += temp
    tempsum *= 8
    tempsum += temp*8
    if i == N-1 :
        print(answer)