def bubble_sort(array):
    lenght = len(array)
    for i in range(lenght - 1, 0 , -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

array = [int(s) for s in input().split()]
print(bubble_sort(array))