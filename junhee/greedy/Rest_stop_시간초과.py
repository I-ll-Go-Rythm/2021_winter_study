L, N, rf, rb = map(int, input().split())
X=[]
C=[]
answer = 0
temp = 0
def find_from_back(arr,num):
    for i in range(len(arr)):
        if arr[len(arr)-i-1] == num:
            return len(arr)-i-1
for i in range(N):
    x, c = map(int, input().split())
    X.append(x)
    C.append(c)
j = -1
while True:
    max_taste = max(C[j+1:])
    j = find_from_back(C,max_taste)
    answer += max_taste*(X[j]-temp)*(rf-rb)
    temp = X[j]
    if j == N-1:
        break
print(answer)