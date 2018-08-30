# Given two binary trees, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
#
# Example 1:
#
# Input:     1         1
#           / \       / \
#          2   3     2   3
#
#         [1,2,3],   [1,2,3]
#
# Output: true
# Example 2:
#
# Input:     1         1
#           /           \
#          2             2
#
#         [1,2],     [1,null,2]
#
# Output: false
# Example 3:
#
# Input:     1         1
#           / \       / \
#          2   1     1   2
#
#         [1,2,1],   [1,1,2]
#
# Output: false

# High level idea :
# Traverse both trees simultaneously and compare nodes at each recursive call. Consider different cases:
#   Case 1: Both nodes at null => Good
#   Case 2: Only one node is null => Bad
#   Case 3: Both nodes not null, but values are different => Bad
#   Case 4: Both nodes not null, same values => Good

class Solution:
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p == None and q == None:
            # reached end of both sub trees
            return True
        if (p == None) or (q == None):
            # if reached end of one but not the other
            return False
        # if both are not none
        if p.val != q.val:
            #nodes aren't the same
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
