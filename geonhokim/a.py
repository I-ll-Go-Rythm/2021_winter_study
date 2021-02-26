def recursion(count, targetNum, currentCount = 0, result = 0, temp_sum = 0, is_index = 0):
    #리턴조건
    if currentCount >= count : return result
    #1부터 12까지
    for k in range(is_index, 12):
        #임시합을 더해본다.
        t_s = temp_sum+k+1
        #더한값이 타겟넘과 같고 더한 횟수가 목표횟수와 같다면 결과에 추가 
        if t_s == targetNum and count == currentCount+1: return result + 1
        #재귀로 계산한다.
        result = recursion(count, targetNum, currentCount+1,result, t_s, k+1)
    return result
 
T = int(input())
for t in range(1, T+1):
    count, targetNum = map(int, input().split())
    result = recursion(count, targetNum)
    print("#{} {}".format(t, result))