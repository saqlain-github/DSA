def merge_sort(list):
    if len(list) <= 1:
        return list
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)
    return merge(left, right)


def split(list):
    mid = len(list)//2
    return list[:mid],list[mid:]

def merge(left, right):
    l = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1

    while i < len(left):
        l.append(left[i])
        i+=1

    while j < len(right):
        l.append(right[j])
        j+=1

    return l

def verify_sort(list):
    if len(list) <= 1:
        return True

    return list[0] < list[1]  and verify_sort(list[1:])


l = merge_sort([2,3,5,1,6,78,8])
print(verify_sort([2,3,4,51,12]))
print(verify_sort(l))
print(l)