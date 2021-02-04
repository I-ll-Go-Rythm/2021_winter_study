rows, columns = map(int,input().split())
input_list = []
for i in range(rows):
    input_list.append(list(input()))
#--------------input받기-------------------------
compare_list = []
for i in range(4):
    compare_list.append(['B','W','B','W','B','W','B','W'])
    compare_list.append(['W','B','W','B','W','B','W','B'])

def check_list(list8): #배열을 인자로 받아 compare_list와 비교해 바꿔야 하는 문자 개수 반환
    answer1 = 0
    answer2 = 0
    for row in range(8):
            for column in range(8):
                if list8[row][column] == compare_list[row][column]:
                    answer1 += 1
                else:
                    answer2 += 1
    if answer1 <= answer2:
        return answer1
    else :
        return answer2

answer = 64 #답으로 나올 수 있는 최대값이 64            

for i in range(rows-7):
    for j in range(columns-7):
        list8 = []
        for k in range(8):
            list8.append(input_list[i:i+8][k][j:j+8])        
        temp = check_list(list8)
        if answer > temp:
            answer = temp

print(answer)