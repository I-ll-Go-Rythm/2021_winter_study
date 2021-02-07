N = int(input())
g = []
for _ in range(N):
    g.append(int(input()))

def sol (a, b):
    if a == b:
        return a
    mid = (a+b)//2
    ret = max(sol(a, mid), sol(mid+1, b))

    left = mid
    right = mid + 1
    min_val = min(left, right)
    width = 2
    ret = max(ret, min_val*width)

    while left > a or right < b:
        if right < b and (left == a or g[left-1]<g[right+1]) :
            right += 1
            width += 1
            min_val = min(min_val, g[right])
        else:
            left -= 1
            width += 1
            min_val = min(min_val, g[left])
        ret = max(ret, min_val*width)
    return ret
print(sol(0, len(g)-1))


