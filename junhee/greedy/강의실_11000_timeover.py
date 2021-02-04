def find_pos(array,num): # n*2의 이차원 배열의 2열과 일치하는 값을 찾아 행의 위치를 반환하는 함수  
    n = len(array)
    while num >= min(map(lambda x : x[1], array)):#time over
        for i in range(n):
            if array[i][1] == num:
                return i
        num -= 1
    return -1
               
number = int(input())
time_list = []
for i in range(number):
    time_list.append(list(map(int,input().split())))
time_list.sort(key = lambda x : (x[1]))
#print(time_list)
lec_list = [time_list[0]]

for time1, time2 in time_list[1:] :
    pos = find_pos(lec_list, time1)
    if pos == -1 :
        lec_list.append([time1,time2])
    else :
        lec_list[pos][1] = time2
        
print(len(lec_list))