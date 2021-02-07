# ara =[[1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 0, 0, 0]]
# last_star=[[3,3,3],[1,0,1],[1,1,1,]]
# for i in range(3):
#         for j in range(3):
#             if i==1 and j ==1:
#                 continue
#             for k in range(3 ):
#                 ara[i*3 +k][j*3 :(j+1)*3 ] = last_star[k] 
# print(ara)

# for i in range(9):
#     for j in range(9):
#         if ara[i][j]==1:
#             print("*", end="")
#         else :
#             print(" ", end="")
#     print()

def draw(H):
    temp=[]
    starlist=[]
    for i in range(H):
        temp.append(0)
    for i in range(H):
        starlist.append(temp)
    h = H//3
    last_star = [[1,1,1],[1,0,1],[1,1,1,]]
    for i in range(3):
        for j in range(3):
            if i==1 and j ==1:
                continue
            for k in range(h):
                starlist[(i*h)+k][(j*h):(j+1)*h] = last_star[k] 
    return starlist
print(draw(9))