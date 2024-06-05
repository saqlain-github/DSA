'''
Insertion sort:
is a simple sorting algorithm that works similar to the way you sort playing cards in your hands.
The array is virtually split into a sorted and an unsorted part. Values from the unsorted part are picked
and placed at the correct position in the sorted part.

Characteristics of Insertion Sort:
- This algorithm is one of the simplest algorithm with simple implementation
- Basically, Insertion sort is efficient for small data values
- Insertion sort is adaptive in nature, i.e. it is appropriate for data sets which are already partially sorted.
'''

# good explanation in notes


def insertionSort(arr):
    for i in range(1,len(arr)):
        val = arr[i]
        j=i-1
        while(j>=0 and val < arr[j]):
            arr[j+1] = arr[j]                                      
            j -= 1
        arr[j+1] = val
    return arr


a = [9,5,1,4,3]

print(insertionSort(a))