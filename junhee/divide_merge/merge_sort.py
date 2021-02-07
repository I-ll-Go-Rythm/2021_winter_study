#블로그 보고 mergesort 만들어봄 꿀잼

a=[5,1,2,3,6,4,8,7,9,10,15,18,12,11,17,13,14,19,16]
def merge_sort(a):
    if len(a)==1:
        return a
    left = a[:int(len(a)/2)]
    right = a[int(len(a)/2):]
    left = merge_sort(left)
    right = merge_sort(right)
    l=0
    r=0
    sorted_list = []
    for i in range(len(a)):
        if l == int(len(a)/2)-1:
            left.append(float("inf"))
        if r == int(len(a)/2):
            right.append(float("inf"))
        if left[l] < right[r]:
            sorted_list.append(left[l])
            l+=1
        else:
            sorted_list.append(right[r])
            r+=1
    return sorted_list

print(merge_sort(a))