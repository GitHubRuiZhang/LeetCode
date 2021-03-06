# python3
# Given a binary tree, find the maximum path sum.

# For this problem, a path is defined as any sequence of nodes from some starting node to
# any node in the tree along the parent-child connections.
# The path must contain at least one node and does not need to go through the root.

# For example:
# Given the below binary tree,

#        1
#       / \
#      2   3
# Return 6.


# My solution
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.out = -float('inf')

    def search(self, root, value):
        if root is None:
            return 0
        left = max(0, self.search(root.left, value))
        right = max(0, self.search(root.right, value))
        self.out = max(self.out, left + right + root.val)
        return root.val + max(left, right)

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.search(root, self.out)
        return self.out


