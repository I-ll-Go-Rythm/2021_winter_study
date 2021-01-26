from itertools import combinations_with_replacement

num = int(input())
input_array = []
for i in range(num):
    input_array.append(int(input()))

Tn_list = []

n=1
while (int(n*(n+1)/2) <= 1000):
    Tn_list.append(int(n*(n+1)/2))
    n += 1

def is_Tn(a):
    for i, j, k in list(combinations_with_replacement(Tn_list,3)):
        if i+j+k == a:
            return 1
    return 0

for i in range(num):
    print(is_Tn(input_array[i]))