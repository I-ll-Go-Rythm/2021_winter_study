in_num = input()
in_num = int(in_num)
digit = 0

def digit_sum(a):
    global digit
    Sum = 0
    while a != 0:
        Sum += a%10
        digit += 1
        a = int(a/10)
    return Sum

digit_sum(in_num)

i = 9*digit
if digit == 1 and in_num % 2 == 0:
    print(int(in_num/2))s
else:
    while i!=-1:
        if i==0:
            print(0)
            break
        if digit_sum(in_num-i) == i:
            print(in_num-i)
            break
        i -= 1