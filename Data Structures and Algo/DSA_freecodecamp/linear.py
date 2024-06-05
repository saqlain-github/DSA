def linear_search(list,target):
    for i in range(0,len(list)):
        if list[i] == target:
            return i
    return None

temp = linear_search([12,3.4,2,3,4,5,6,7,87],10)
print(temp)