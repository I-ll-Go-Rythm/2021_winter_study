def compare(s,a):
    for word in a:
        if s.find(word) == 0 and iseither(s,len(word)) :
            return 1
    else :
        return 0
def iseither(s,i): #문자열 s의 i번째 이후의 문자열이 문제 조건을 만족하는지 안하는지를 반환
    global A
    if i==len(s):
        return 1
    if compare(s[i:],A) == 0:
        return 0
    else:
        return 1 

dp = [0]*101

S = input()
N = int(input())
A = [input() for _ in range(N)]
A.sort(key=lambda x : -len(x))
print(compare(S,A))