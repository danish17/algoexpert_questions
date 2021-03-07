# O(n^2) time -- O(1) space since it is inplace
def bubbleSort(array):
    # Write your code here.
    nIdx = 0
    mIdx = 0
    for nIdx in range(0, len(array)):
        for mIdx in range(0, len(array)):
            if array[nIdx] < array[mIdx]:
                swap = array[nIdx]
                array[nIdx] = array[mIdx]
                array[mIdx] = swap
    return array

bubbleSort([5,4,3,2,1])