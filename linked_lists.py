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
        print(curNode)

##      /////////////////////////////    ##

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
        print("lsat swap", slowRunner, self.tail)
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
    def splitHelper(self, start, splitPoint):
        count = 1
        curNode = start
        while (count != splitPoint):
            curNode = curNode.next
            count += 1
        #reached splitPoint
        print(curNode.data)
        newHead = curNode.next
        curNode.next = None
        newHead.previous = None
        #make a new linked list, return that head
        newList = linkedList
        #insert newhead into new linked list (currently empty)
        newList.head = newHead
        #traverse the down new list to find the tail
        tailNode = newHead
        while tailNode.next:
            tailNode = tailNode.next
        newList.tail = tailNode
        return newList

    #insert a new node right after a specified node
def insertAfterNode(node, data):
    newNode = Node(data)
    nextNode = node.next #could be null
    #lhs
    node.next = newNode
    newNode.previous = node
    #rhs
    newNode.next = nextNode
    if nextNode:
        nextNode.previous = newNode

#given two sorted lists,, return a single sorted list with all
def merge(lst1, lst2):
    #assign curListPtr to be the list with the lower starting number
    curListPtr = lst1.head if lst1.head.data < lst2.head.data else lst2.head
    otherListPtr = lst1.head if lst1.head != curListPtr else lst2.head
    returnHead = lst1 if lst1.head.data < lst2.head.data else lst2
    # curListPtr = curListPtr.next
    while curListPtr.next and otherListPtr:
        if curListPtr.next.data < otherListPtr.data:
            curListPtr = curListPtr.next
        else:
            insertAfterNode(curListPtr, otherListPtr.data)
            otherListPtr = otherListPtr.next
            curListPtr = curListPtr.next
    if curListPtr.next == None:
        #join the rest of other list
        while (otherListPtr != None):
            insertAfterNode(curListPtr, otherListPtr.data)
            curListPtr = curListPtr.next
            otherListPtr = otherListPtr.next
    return returnHead


#driver code
lst1 = linkedList()
lst2 = linkedList()
for x in range (0,1):
    lst1.insertBack(2*x + 1)

for x in range(2,4):
    lst2.insertBack(x)

lst1.display()
lst2.display()

lst3 = merge(lst1, lst2)
lst3.display()
