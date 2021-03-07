def spiralTraverseHelper(array, startCol, startRow, endCol, endRow, spiral):
    if startRow > endRow or startCol > endCol:
        return
    else:
        for idx in range(startCol, endCol + 1):
            spiral.append(array[startRow][idx])
        for idx in range(startRow + 1, endRow + 1):
            spiral.append(array[idx][endCol])
        for idx in reversed(range(startCol, endCol)):
            if startRow == endRow:
                break
            spiral.append(array[endRow][idx])
        for idx in reversed(range(startRow + 1, endRow)):
            if startCol == endCol:
                break
            spiral.append(array[idx][startCol])
        spiralTraverseHelper(array, startCol + 1, startRow + 1, endCol - 1, endRow - 1, spiral)

def spiralTraverse(array):
    # Write your code here.
    spiral = []
    n = len(array) - 1
    m = len(array[0]) - 1
    spiralTraverseHelper(array, 0, 0, m, n, spiral)
    return spiral

array = [[1, 2, 3],
         [8, 9, 4],
         [7, 6, 5]]

spiralTraverse(array)