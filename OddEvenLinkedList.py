# Given a singly linked list, group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.
#
# You should try to do it in place. The program should run in O(1) space
# complexity and O(nodes) time complexity.

#  EX.
# Input: 1->2->3->4->5->NULL
# Output: 1->3->5->2->4->
# Input: 2->1->3->5->6->4->7->NULL
# Output: 2->3->6->7->1->5->4->NULL

# General idea: iterate through the linked list and store the first even node in a local variable
# continuously store the pointers to the nodes

def oddEven(list):
    if not list.head.next.next:
        #list has one item, already seperated
        return list
    evenListPtr = list.head.next.next #2nd valid node
    curNode = list.head.next #start at 1st valid node
    count = 1 #to keep track of whether we're on an odd or even node
    #iterate through list
    while curNode.next.next:
        nextTemp = curNode.next
        #link curNode to the the next odd/even node respectively
        curNode.next = curNode.next.next
        #now iterate to the compliment set
        curNode = nextTemp
        count += 1
    #we have now terminated our while loop at the ultimate node after setting the
    #penultimate (last even node) to null
    #now join the last node in the odd list to the beginning of the even list
    #we stored in evenListPtr
    if count % 2 == 0:
        #ended on even, so increment once
        #this handles the case of an odd lengthed list, which our
        #algorithm misses
        temp = curNode.next
        curNode.next = None
        curNode = temp

    #ended on odd, listLen is even!
    print('here')
    curNode.next = evenListPtr
    return list


###############################
## LINKEDLIST CODE
import random

class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = Node()
    def display(self):
        elements = []
        curNode = self.head
        while curNode.next != None:
            curNode = curNode.next
            elements.append(curNode.data)
        print (elements)
        return len(elements)
    def append(self, data):
        curNode = self.head
        newNode = Node(data)
        while curNode.next != None:
            #traverse to the end of the linked list
            curNode = curNode.next
        curNode.next = newNode

###############################
## DRIVER CODE
myList = linkedList()
for i in range (1,6):
    myList.append(i)
myList.display()
myNewList = oddEven(myList)
myNewList.display()
