def sol(s,e):
    if s == e:
        return A[s]**2
    mid = (s+e)//2
    l = mid
    r = mid +1
    t_sum = (A[l]+A[r])
    m_score = min(A[l],A[r])
    max_score = max(sol(s,l), sol(r,e),t_sum*m_score)
    
    while l > s or r < e:
        if r < e and (A[l-1]<=A[r+1] or l==s):
            m_score = min(m_score, A[r+1])
            t_sum += A[r+1]
            max_score = max(max_score, t_sum*m_score)
            r += 1
        else:
            m_score = min(m_score, A[l-1])
            t_sum += A[l-1]
            max_score = max(max_score, t_sum*m_score)
            l -= 1
                 
    return max_score

N = input()
A = list(map(int, input().split()))

print(sol(0,len(A)-1))