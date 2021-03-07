# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def nodeDepths(root):
    # Write your code here.
    sum = calcNodeDepth(root, 0)
    return sum


def calcNodeDepth(root, depth):
    if root is None:
        return 0
    depth += calcNodeDepth(root.right, depth+1) + calcNodeDepth(root.left, depth+1)
    return depth