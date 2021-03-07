# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    currNode = linkedList
    while currNode is not None:
        currVal = currNode.value
        nextVal = currNode.next.value
