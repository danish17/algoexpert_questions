# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    sums = []
    branchSumsHelper(root, 0, sums)
    return sums

def branchSumsHelper(root, sum, sumList):
    if root is None:
        return

    newRunSum = sum + root.value
    if root.right is None and root.left is None:
        sumList.append(newRunSum)
        return sumList

    branchSumsHelper(root.left, newRunSum, sumList)
    branchSumsHelper(root.right, newRunSum, sumList)

