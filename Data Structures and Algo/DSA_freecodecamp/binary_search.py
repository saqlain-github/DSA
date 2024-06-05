def binary_search(list,target):
    first, last = 0, len(list)-1
    while first <= last:
        mid = (first+last)//2  #floor divison operator
        if list[mid] == target:
            return mid
        elif list[mid] < target:
            first = mid+1
        else:
            last = mid-1
    return None


temp = binary_search([1,2,3,4,5,6,7,8,9],2)
print(temp)
