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
        self.length = 0
    def display(self):
        curNode = self.head
        while (curNode):
            print(curNode.data, end =" ")
            curNode = curNode.next
        print(curNode)

##      /////////////////////////////    ##
##      The following questions will assume a LL with a dummy head Node

    def insertFront(self, data):
        #empty BASECASE
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
    def insertBack(self, data):
        #empty basecase
        if not self:
            newNode = Node(data)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(data)
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode

    def reverseHelper(self, start, end):
        leftAnchor = start.previous #could be null
        # print(leftAnchor.data)
        rightAnchor = end.next #could be null
        # print(rightAnchor)
        self.reverse(start, end)
        if (start == self.head):
            # print("ping start")
            self.head = end
        if (end == self.tail):
            # print("ping end")
            self.tail = start
        #reanchor the nodes
        if leftAnchor:
            leftAnchor.next = end
            # print('leftanchors', leftAnchor.next.next.next.next.next.next   )
        end.previous = leftAnchor
        if rightAnchor:
             rightAnchor.previous = start
             # print('anchors', rigtAnchor)
        start.next = rightAnchor
        # print('right anchor', start)
        # print("end.next", end.next)
        # print("end", end)
        # print("leftAnchor", leftAnchor, leftAnchor.next)
        # print('lst head', self.head.next)

    def reverse(self, node, end):
        current = node
        # print ("start, end", node, end)
        next = None
        prev = None
        while current != end:
            next = current.next #could be null
            prev = current.previous #could be null
            current.previous = next
            current.next = prev
            #iterate
            # current.next and print(current.next.data, end=" ")
            current = next
        #since we stopped at the penultimate node, we must also reverse the last
        # node
        end.next = current.previous
    def reverseNth(self, n):
        #given a linked list reverse blocks of n elements in list
        fastRunner = self.head
        slowRunner = self.head
        counter = 1
        while (fastRunner and fastRunner != self.tail):
            if counter % n == 0:
                cont = fastRunner.next
                # print("in if", slowRunner, fastRunner)
                self.reverseHelper(slowRunner, fastRunner)
                slowRunner = cont
                fastRunner = cont.next
                continue
            fastRunner = fastRunner.next
            # print(fastRunner.data)
            counter += 1
        print("lsat swap", slowRunner, self.tail)
        self.reverseHelper(slowRunner, self.tail)


#driver code
lst = linkedList()
for x in range (0,6):
    lst.insertFront(random.randint(0,10))

lst.display()
lst.reverseNth(2)
lst.display()
