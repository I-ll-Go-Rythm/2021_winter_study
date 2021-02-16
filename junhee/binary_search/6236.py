import sys
input = sys.stdin.readline
n,m=map(int,input().split())
money=[]
for _ in range(n):
  money.append(int(input()))
summy=sum(money)
start, end = 0,summy
result=summy

while start<=end:
    mid = (start+end)//2
    temp=mid
    flag=False
    cnt=1
    for i in range(n):
      if mid<money[i]:
        flag=True
        break
      if temp<money[i]:
        temp=mid
        cnt+=1
      temp-=money[i]

    if flag ==False:
      if cnt<=m:
        end = mid-1
        if mid<result:
          result = mid
      else:
        start = mid+1
    else:
      start = mid+1

print(result)