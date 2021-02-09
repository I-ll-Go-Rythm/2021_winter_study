def draw(H):
    if H == 3:
        return [['*','*','*'],['*',' ','*'],['*','*','*']]
    temp=[]
    starlist=[]
    for i in range(H):
        temp.append(0)
    for i in range(H):
        starlist.append(temp)#temp를 바꾸면 starlist도 바뀜
    h = H//3
    last_star = draw(h)
    for i in range(3):
        for j in range(3):
            if i==1 and j ==1:
                continue
            for k in range(h):
                starlist[(i*h)+k][(j*h):(j+1)*h] = last_star[k] 
    return starlist
N = int(input())

star = draw(N)

for i in range(N):
    for j in range(N):
        if star[i][j]==1:
            print("*", end="")
        else :
            print(" ", end="")
    print()