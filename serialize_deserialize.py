
# Given the root to a binary tree, implement serialize(root), which serializes the tree
# into a string, and deserialize(s), which deserializes the string back into the tree.

#   HIGH LEVEL
#   serialize: use a pre-order traversal to maintain tree structure. if nodes
#   are null, use '/' as a marker to denote the end of the branch
#   deserialize: build the tree recursively, scopes are tricky.

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

test = Node('a', Node('b'), Node('c'))

def display(root):
    if root == None:
        return
    print(root.val)
    display(root.left)
    display(root.right)


def serialize(root):
    #serialize the tree
    str=""
    def recurse(node):
        #user str from outer scope
        nonlocal str
        if node == None:
            str += '/'
            return
        str += node.val
        recurse(node.left)
        recurse(node.right)
    recurse(root)
    return str


def deserialize(str):
    #deserialize the tree
    chars = str
    #use i as a closure variable
    i = -1
    def rec():
        nonlocal i
        i += 1
        if i == len(chars):
            return
        if chars[i] == '/':
            return
        #use constructor recursively
        return Node(chars[i], rec(), rec())
    return rec()
