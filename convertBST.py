# Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original
# BST is changed to the original key plus sum of all keys greater than the original key in BST.

# ex
# Input: The root of a Binary Search Tree like this:
#               5
#             /   \
#            2     13
#
# Output: The root of a Greater Tree like this:
#              18
#             /   \
#           20     13

# High Level Idea:
# Use a depth first search to the very right node, and traverse the tree in descending order
# Keep a running total global variable called running sum that is accessable by each recursive call,
# and increase the current root's value by running sum at each function call.

# NOTE. Since variables in Python are immutable, we are declaring runningSum as a list instead--
# lists are mutable so this solves the issue.

class Solution:
    def convertBST(self, root):
        # lists are mutable
        runningSum = [0]
        return self.helper(root, runningSum)

    #recursive function
    def helper(self, root, runningSum):
        if root == None:
            return
        #traverse all the way down to the right (greatest element)
        self.helper(root.right, runningSum)
        curVal = root.val
        root.val += runningSum[0]
        runningSum[0] += curVal
        self.helper(root.left, runningSum)
        #return value is just for the convertBST function
        return root
