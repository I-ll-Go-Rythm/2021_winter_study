def findmid(hs):#중간에 걸친 직사각형 찾는 함수
    j = int(len(hs)/2)
    l=1
    r=1
    max_h = hs[j]
    mid_max = max_h
    if (len(hs)%2 != 0):
        for i in range(2,len(hs)+1):
            if r == j+1 :
                if hs[j-l]< max_h:
                    max_h = hs [j-l]
                if mid_max < max_h*i:
                    mid_max = max_h*i
                l += 1
                continue
            if l == j+1:
                if hs[j+r]< max_h:
                    max_h = hs[j+r]
                if mid_max < max_h*i:
                    mid_max = max_h*i
                r += 1
                continue
            if hs[j+r]>hs[j-l]:
                if hs[j+r]< max_h:
                    max_h = hs[j+r]
                if mid_max < max_h*i:
                    mid_max = max_h*i
                r += 1
            else:
                if hs[j-l]< max_h:
                    max_h = hs [j-l]
                if mid_max < max_h*i:
                    mid_max = max_h*i
                l += 1
            if max_h == 1 :
                if mid_max < len(hs):
                    return len(hs)
                break
    else:
        if hs[j]>hs[j-1]:
            mid_max = hs[j-1]*2
            max_h = hs[j-1]
        else:
            mid_max = hs[j]*2
            max_h = hs[j]
        l=2
        for i in range(3,len(hs)+1):
            if r == j :
                if hs[j-l]< max_h:
                    max_h = hs [j-l]
                if mid_max < max_h*i:
                    mid_max = max_h*i
                l += 1
                continue
            if l == j+1:
                if hs[j+r]< max_h:
                    max_h = hs[j+r]
                if mid_max < max_h*i:
                    mid_max = max_h*i
                r += 1
                continue
            if hs[j+r]>hs[j-l]:
                if hs[j+r]< max_h:
                    max_h = hs[j+r]
                if mid_max < max_h*i:
                    mid_max = max_h*i
                r += 1
            else:
                if hs[j-l]< max_h:
                    max_h = hs [j-l]
                if mid_max < max_h*i:
                    mid_max = max_h*i
                l += 1
            if max_h == 1 :
                if mid_max < len(hs):
                    return len(hs)
                break
    return mid_max
print(findmid([1,1,1,1,1,2,2,2,1,1,1,1,1]))