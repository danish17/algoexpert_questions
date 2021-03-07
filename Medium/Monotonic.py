def isMonotonic(array):
    idx = 0
    for idx in range(len(array) - 1):
        if array[idx] == array[idx + 1]:
            idx += 1
        elif array[idx] < array[idx + 1]:  # increasing
            for idxTwo in range(idx + 1, len(array)):
                if array[idxTwo] < array[idxTwo - 1]:
                    return False
        elif array[idx] > array[idx + 1]:  # decreasing
            for idxTwo in range(idx + 1, len(array)):
                if array[idxTwo] > array[idxTwo - 1]:
                    return False
    return True

isMonotonic([1,2,3,4,5,6,7,8,9])