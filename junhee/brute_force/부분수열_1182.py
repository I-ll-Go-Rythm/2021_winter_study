from itertools import combinations

temp = input().split(" ")
number = int(temp[0])
Sum = int(temp[1])
input_list = input().split(" ")

answer = 0

for i in range(1, number+1):
    i_list = list(combinations(input_list,i))
    length = len(i_list)
    for j in range(length):
        if sum(map(int, i_list[j])) == Sum:
            answer += 1
print(answer)            