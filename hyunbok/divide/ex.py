a, b = map(int, input().split())
def sol(a, b):
    if a == 1 and b == 1:
        return('right!')
        
    for i in range(a):
        for j in range(b):
            sol(1, 1)
    return
print(sol(a, b))
