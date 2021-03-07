def binarySearch(array, target):
    return binarySearchHelper(array, target, 0, len(array) - 1)

def binarySearchHelper(array, target, left, right):
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if target == array[mid]:
            return mid
        elif target > array[mid]:
            return binarySearchHelper(array, target, mid + 1, right)
        else:
            return binarySearchHelper(array, target, left, mid - 1)
