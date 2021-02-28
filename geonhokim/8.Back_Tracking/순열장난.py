import sys
from collections import deque

def backTracking(k):
    if k == len(N):
        max_num = 0
        for i in range(len(arr)):
            max_num = max(max_num, int(arr[i]))
        
        if max_num == len(arr):
            for i in range(len(arr)):
                print(int(arr[i]), end = ' ')
            sys.exit()
        return
    
    if k < len(N) and 0 < int(N[k]) <= 50 and not isVisit[int(N[k])]:
        isVisit[int(N[k])] = 1
        arr.append(N[k])
        backTracking(k + 1)
        arr.pop()
        isVisit[int(N[k])] = 0
    
    if k + 1 < len(N) and 0 < int(N[k: k+2]) <= 50 and not isVisit[int(N[k: k+2])]:
        isVisit[int(N[k: k+2])] = 1
        arr.append(N[k: k+2])
        backTracking(k + 2)
        arr.pop()
        isVisit[int(N[k: k+2])] = 0

arr = deque()
N = input()
isVisit = [0] * 51

backTracking(0)