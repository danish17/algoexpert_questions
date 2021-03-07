def insertionSort(array):
    for i in range(len(array)):
        for j in range(len(array)):
            if array[i] < array[j]:
                swap(i, j, array)
    return array

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]
