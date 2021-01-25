def solution(phone_book):
    answer = True
    phone_book.sort()
    for i in range(len(phone_book)):
        j=i+1
        if answer == False :
            break
        while j < len(phone_book):
            if phone_book[i] == phone_book[j][0:len(phone_book[i])]:
                answer = False
                break
            else :
                j += 1
    
    return answer