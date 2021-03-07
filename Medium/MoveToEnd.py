def moveElementToEnd(array, toMove):
    # array.sort() Not required, since order is immaterial
    idx = 0
    last = len(array) - 1
    while idx < last:
        if array[idx] != toMove:
            idx += 1
        elif array[idx] == toMove and array[last] != toMove:
            array = moveToLast(array, idx, last)
            last -= 1
        elif array[idx] == toMove and array[last] == toMove:
            last -= 1
            array = moveToLast(array, idx, last)
    return array

def moveToLast(array, idx, last):
    array[idx], array[last] = array[last], array[idx]
    return array

moveElementToEnd(['A', 'B', 'C', 'C', 'D', 'C', 'D', 'A'], 'C')