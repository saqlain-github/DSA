def recurssive_binary(list,target):
    if len(list) == 0:
        return False
    else:
        mid = (len(list))//2
        if list[mid] == target:
            return True
        else:
            if list[mid]<target:
                return recurssive_binary(list[mid+1:],target)
            else:
                return recurssive_binary(list[:mid],target)

print(recurssive_binary([1,2,3,4,5,6,7,8,9],10))
