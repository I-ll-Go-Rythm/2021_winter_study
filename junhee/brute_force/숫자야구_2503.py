from itertools import permutations

num = int(input())

digits = []
for i in range(num):
    a = list(input())
    digits.append(a)

answer = 0

for i in list(permutations(['1','2','3','4','5','6','7','8','9'],3)):
    candidate = list(i)
    for j in range(num):
        strike = 0
        ball = 0
        for k in range(3):
            if candidate[k] == digits[j][k]:
                strike += 1
            elif candidate[k] in digits[j]:
                ball += 1
        if strike != int(digits[j][4]) or ball != int(digits[j][6]):
            break
        if j == num-1:
            answer += 1
print(answer)                    