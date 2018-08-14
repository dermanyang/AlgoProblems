#class declaration
import random
class Node:
    def __init__(self, data= None):
        self.data = data
        self.next = None
        self.previous = None
class linkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def display(self):
        curNode = self.head
        while (curNode):
            print(curNode.data, end =" ")
            curNode = curNode.next


##      // methods

    #insert a node at the front of the list
    def insertFront(self, data):
        #empty case: head and tail both point to the new node
        if not self.head:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        #non-empty case
        else:
            newNode = Node(data)
            self.head.previous = newNode
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    #insert a node at the end of the list
    def insertBack(self, data):
        #empty basecase
        if not self.head:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        #non-empty basecase
        else:
            newNode = Node(data)
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    #reverse a linked list from a start node and a beginnig node
    def reverseHelper(self, start, end):
        #determine anchors. these are the nodes immediately to the left / right of the reversed region
        leftAnchor = start.previous #could be null
        rightAnchor = end.next #could be null
        #call to reverse
        self.reverse(start, end)
        #deal with edge cases. if either ends of the reversed region are the head/tail, we must
        #update the head/tail respectively
        if (start == self.head):
            self.head = end
        if (end == self.tail):
            self.tail = start
        #reanchor the nodes. reattach the reversed area back with the anchors
        if leftAnchor:
            leftAnchor.next = end
        end.previous = leftAnchor
        if rightAnchor:
             rightAnchor.previous = start
        start.next = rightAnchor

    #reverse an entire linked list
    def reverse(self, node, end):
        current = node
        next = None
        prev = None
        while current != end:
            next = current.next #could be null
            prev = current.previous #could be null
            current.previous = next
            current.next = prev
            #iterate
            current = next
        #since we stopped at the penultimate node, we must also reverse the last
        # node
        end.next = current.previous

    #given a linked list reverse blocks of n elements in list
    def reverseNth(self, n):
        fastRunner = self.head
        slowRunner = self.head
        counter = 1
        while (fastRunner and fastRunner != self.tail):
            if counter % n == 0:
                cont = fastRunner.next
                self.reverseHelper(slowRunner, fastRunner)
                slowRunner = cont
                fastRunner = cont.next
                continue
            fastRunner = fastRunner.next
            # print(fastRunner.data)
            counter += 1
        # print("lsat swap", slowRunner, self.tail)
        self.reverseHelper(slowRunner, self.tail)

    #   every other node (starting from the second node)
    #   is removed from the list and appended to the back (new tail)
    #   do this until the next node to be removed is the tail or null
    def waterfall(self):
        index = 1
        curNode = self.head
        while curNode and curNode != self.tail:
            if index % 2 == 0:
                temp = curNode.next
                self.insertBack(curNode.data)
                self.remove(curNode)
                curNode = temp
                index += 1
                continue
                # return
            index += 1
            curNode = curNode.next

    #given a node, remove it from the linked list
    def remove(self, cur):
        #if front of list
        if cur == self.head:
            self.head = cur.next
            self.head.previous = None
            return
        #if on tail of list
        if cur == self.tail:
            self.tail = cur.previous
            cur.previous.next = None
            return
        #else, if in torso
        prev = cur.previous
        prev.next = cur.next
        cur.next.previous = prev

    #given a linked list, return a new linked list starting from splitPoint
    #number of nodes from start
def splitHelper(start, splitPoint):
    count = 1
    curNode = start
    while (count < splitPoint):
        curNode = curNode.next
        count += 1
    #reached splitPoint
    newHead = curNode.next
    curNode.next = None
    newHead.previous = None
    return newHead


##      // mergesort functions

#insert a new node right after a specified node
def insertAfterNode(node, data):
    newNode = Node(data)
    # print('ping')
    nextNode = node.next #could be null
    #lhs
    node.next = newNode
    newNode.previous = node
    #rhs
    newNode.next = nextNode
    if nextNode != None:
        nextNode.previous = newNode
    return newNode

#given two sorted lists,, return a single sorted list with all
def merge(lst1, lst2):
    #assign curListPtr to be the list with the lower starting number
    if lst1 == None:
        return lst2
    if lst2 == None:
        return lst1
    curListPtr = lst1 if lst1.data < lst2.data else lst2
    otherListPtr = lst1 if lst1 != curListPtr else lst2
    returnHead = lst1 if lst1.data < lst2.data else lst2
    # curListPtr = curListPtr.next
    while curListPtr.next and otherListPtr:
        if curListPtr.next.data <= otherListPtr.data:
            curListPtr = curListPtr.next
        else:
            temp1 = otherListPtr.next
            temp2 = insertAfterNode(curListPtr, otherListPtr.data)
            otherListPtr = temp1
            curListPtr = temp2
    if curListPtr.next == None:
        #join the rest of other list
        while (curListPtr and otherListPtr != None):
            temp1 = otherListPtr.next
            temp2 = insertAfterNode(curListPtr, otherListPtr.data)
            otherListPtr = temp1
            curListPtr = temp2
    return returnHead

def merge2(lst1, lst2):
    if lst1 == None:
        return lst2
    if lst2 == None:
        return lst1
    curListPtr = lst1 if lst1.data < lst2.data else lst2
    otherListPtr = lst1 if lst1 != curListPtr else lst2
    returnList = linkedList()
    while curListPtr and otherListPtr:
        if curListPtr.data <= otherListPtr.data:
            returnList.insertBack(curListPtr.data)
            curListPtr = curListPtr.next
        else:
            returnList.insertBack(otherListPtr.data)
            otherListPtr = otherListPtr.next
    if curListPtr == None:
        #join the rest of other list
        while (otherListPtr != None):
            returnList.insertBack(otherListPtr.data)
            otherListPtr = otherListPtr.next
    return returnList.head



def length(start):
    curNode = start
    count = 0
    while curNode :
        count += 1
        curNode = curNode.next
    return count

import math

def mergesort(start):
    if start == None:
        return Node(-1)
    if length(start) == 1:
        return start
        #list length 1, already sorted, return
    len = length(start)
    # print("length", math.floor(len/2))
    left = start
    right = splitHelper(left, math.floor(len/2))
    l = mergesort(left)
    r = mergesort(right)
    print("left", end =" ")
    displayNode(l)
    print("")
    print("right", end =" ")
    displayNode(r)
    print("")
    temp = merge(l,r)
    print("merged ", end="")
    displayNode(temp)
    print("")
    return merge2(l, r)

def displayNode(start):
    curNode = start
    while curNode:
        print (curNode.data, end=" ")
        curNode = curNode.next

# driver code
lst1 = linkedList()
lst2 = linkedList()
    # lst1.insertBack(x)
lst1.insertBack(5)
lst1.insertBack(9)
# lst1.insertBack(9)
lst1.insertBack(2)
lst1.insertBack(3)
# lst2.insertBack(3)

lst1.display()
print("")
# lst2.display()
# print("")
# temp = merge(lst1.head, lst2.head)
# displayNode(temp)
temp = mergesort(lst1.head)
displayNode(temp)
