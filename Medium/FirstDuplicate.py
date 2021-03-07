def firstDuplicateValue(array):
    idx = 0
    for idx in range(len(array)):
        if array[idx] > 0 and array[idx] in array[:idx]:
            return array[idx]
    return -1

firstDuplicateValue([2,1,5,3,3,2,4])