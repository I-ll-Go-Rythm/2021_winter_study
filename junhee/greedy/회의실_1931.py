number = int(input())
time_list = []
answer = 1 # 답은 최소 1
for i in range(number):
    time_list.append(list(map(int,input().split())))
time_list.sort(key = lambda x : (x[1], x[0]))

#2차원 배열에 입력 후 2번째 숫자를 첫 번째 기준으로 오름차순 정렬, 
# 1번째 숫자를 두 번째 기준으로 오름차순 정렬

temp = time_list[0][1]

for i in range(number-1):
    if time_list[i+1][1] == temp :
        if temp == time_list[i+1][0]:
            answer += 1
    elif time_list[i+1][0]>=temp:
        answer += 1
        temp = time_list[i+1][1]
print(answer)