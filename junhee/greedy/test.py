number = int(input())
time_list=[]
for i in range(number):
    time_list.append(list(map(int,input().split())))
time_list.sort(key = lambda x : x[0])
print(time_list)