
def sol(x, y, N, r, c, temp):
    if N != 2:
        if r>= temp + (N//2) and c >= temp + (N//2):
            temp = temp+pow(N, 2)*3//4
            return sol(x + N//2, y + N//2, N//2, r, c, temp)
        
        elif r>= temp + (N//2) and c < temp + (N//2):
            temp = temp+pow(N, 2)*2//4
            return sol(x+N//2, y, N//2, r, c, temp)
        
        elif r< temp + (N//2) and c>= temp + (N//2):
            temp = temp+pow(N, 2)*1//4
            return sol(x, y+N//2, N//2, r, c, temp)
        
        else:
            temp = temp
            return sol(x, y, N//2, r, c, temp)
    else:
        if r==x and c==y:
            return temp
        elif r==x and c==y+1:
            return temp+1
        elif r==x+1 and c==y:
            return temp+2
        else:
            return temp+3

n, r, c = map(int, input().split())
N = pow(2, n)

print(sol(0, 0, N, r, c, 0))


