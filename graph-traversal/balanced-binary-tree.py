# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def postorder_recursive(node):
            if not node:
                return 0
            
            l = postorder_recursive(node.left)
            if l == -1:
                return -1
            r = postorder_recursive(node.right)
            if r == -1:
                return -1
            if abs(l - r) > 1:
                return -1

            return max(l, r) + 1
        return postorder_recursive(root) != -1

            

        


        


        
        