def sorted(values):
    sorted_list = []
    for i in range(0,len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))

    return sorted_list

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = 1
    return min_index

list = sorted([1,3,2,5,6])
print(list)