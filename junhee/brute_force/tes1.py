compare_list1 = []
list8 = []
for i in range(4):
    compare_list1.append(['B','W','B','W','B','W','B','W'])
    compare_list1.append(['W','B','W','B','W','B','W','B'])
input_list =[['a','b','c','d'],['f','b','c','d'],['a','b','c','d'],['a','b','c','d']]

for i in range(2):
    for j in range(2):
        list8 = []
        for k in range(3):
            list8.append(input_list[i:i+3][k][j:j+3])
        print(list8)