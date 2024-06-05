def quickSort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
    print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quickSort(less_than_pivot)+[pivot]+quickSort(greater_than_pivot)


numbers = [9,77,5,1,12,45,3,2,4,5,6]
print(numbers)
sorted_numbers = quickSort(numbers)
print(sorted_numbers)