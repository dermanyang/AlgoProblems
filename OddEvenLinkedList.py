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
    while curNode.next.next:
        nextTemp = curNode.next
        curNode.next = curNode.next.next
        curNode = nextTemp
        count += 1
    # stops at penultimate node
    if count % 2 == 0:
        #ended at an even node #, so increment once.
        #this handles the case of an odd lengthed list, which our
        #algorithm misses
        temp = curNode.next
        curNode.next = None
        curNode = temp

    #ended on odd, listLen is even!
    print('here')
    curNode.next = evenListPtr
    return list


## TIME & SPACE COMPLEXITY
## This algorithm executes in one parse, so it takes O(nodes) time
## Uses O(1) space
