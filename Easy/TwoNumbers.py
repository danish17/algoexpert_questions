# O(n^2) time | O(1) space
def twoNumberSum(array, targetSum):
    twoArr = []
    for i in range(0, len(array)):
        found = False
        for j in range(0, len(array)):
            if i != j:
                if array[i] + array[j] == targetSum:
                    twoArr.extend([array[i], array[j]])
                    found = True
                    break
        if found:
            break
    return twoArr