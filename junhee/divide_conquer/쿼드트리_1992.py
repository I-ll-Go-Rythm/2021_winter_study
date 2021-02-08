def quad(arr):
    if len(arr) == 1:
        return arr[0][0]
    else:
        L = len(arr)//2 
        ls1 = quad([row[:L] for row in arr[:L]])
        ls2 = quad([row[L:] for row in arr[:L]])
        ls3 = quad([row[:L] for row in arr[L:]])
        ls4 = quad([row[L:] for row in arr[L:]])
        if ls1 == 0 and ls1 == ls2 and ls2 ==ls3 and ls3 == ls4:
            return ls1
        if ls1 == 1 and ls1 == ls2 and ls2 ==ls3 and ls3 == ls4:
            return ls1
        else:
            return '({}{}{}{})'.format(ls1,ls2,ls3,ls4)
N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input())))
print(quad(arr))