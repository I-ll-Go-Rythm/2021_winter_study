def posi(N,r,c):
    if r < 2**(N-1):
        if c <2**(N-1):
            return 0
        else:
            return 1
    elif c <2**(N-1):
        return 2
    else:
        return 3
def lastnrc(N,r,c):
    p = posi(N,r,c)
    if p==0:
        return(N-1,r,c)
    elif p ==1:
        return(N-1,r,c-2**(N-1))
    elif p ==2:
        return(N-1,r-2**(N-1),c)
    else :
        return(N-1,r-2**(N-1),c-2**(N-1))
print(posi(1,0,1))