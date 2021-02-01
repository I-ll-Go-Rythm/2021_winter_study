def find_pos(array,num):
    n = len(array)
    for i in range(n):
        if array[i][1] <= num:
            return i
    return -1
               
number = int(input())
time_list = []
for i in range(number):
    time_list.append(list(map(int,input().split())))
time_list.sort(key = lambda x : x[0])

lec_list = [time_list[0]]

for time1, time2 in time_list[1:] :
    pos = find_pos(lec_list, time1)
    if pos == -1 :
        lec_list.append([time1,time2])
    else :
        lec_list[pos][1] = time2
        
print(len(lec_list))