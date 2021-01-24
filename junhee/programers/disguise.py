def solution(clothes):

    clothes_dic={}
    
    for name, kind in clothes:
        if kind in clothes_dic:
            clothes_dic[kind] += 1
        else:
            clothes_dic[kind] = 1
    
    answer = 1
    
    for i in clothes_dic.values():
        answer = answer*(i+1)
    
    answer = answer-1
    return answer