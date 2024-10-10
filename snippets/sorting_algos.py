a = [12, 45, 23, 89, 31]

# bubble sort
def bubble_sort(arr, size):
    for i in range(size):
        for j in range(0, size-i-1):
            if arr[j] > arr[j+1]:                                      
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

# print(bubble_sort(a, len(a)))


# selection sort
def bubble_sort(arr, size):              
    for s in range(size):
        min_index = s

        for 