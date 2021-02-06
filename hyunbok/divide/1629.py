def sol(a, b):
    if b == 1:
        return a%c
    elif b == 2:
        return a*a%c
    else:
        temp = sol(a, b//2)
        if b%2==0:
            return temp*temp%c
        else:
            return temp*temp*a%c

a, b, c = map(int, input().split())

ans = sol(a, b)

print(ans)

