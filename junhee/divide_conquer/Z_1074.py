def posi(N,r,c): #전체를 기준으로 몇 사분면에 위치하는지 반환(1사분면 : 0, 2사분면 : 1 ...)
    if r < 2**(N-1):
        if c <2**(N-1):
            return 0
        else:
            return 1
    elif c <2**(N-1):
        return 2
    else:
        return 3
def lastnrc(N,r,c):#전 단계(2^N-1)에서는 N,r,c가 몇 인지를 튜플로 반환.
    p = posi(N,r,c)
    if p==0:
        return(N-1,r,c)
    elif p == 1:
        return(N-1,r,c-2**(N-1))
    elif p == 2:
        return(N-1,r-2**(N-1),c)
    elif p == 3:
        return(N-1,r-2**(N-1),c-2**(N-1))
def find(tup):
    if tup[0] == 1:
        return posi(tup[0],tup[1],tup[2])
    last_ans = find(lastnrc(tup[0],tup[1],tup[2]))
    return last_ans + (2**(2*tup[0]-2))*posi(tup[0],tup[1],tup[2])

N, r, c = map(int, input().split())

print(find((N,r,c)))