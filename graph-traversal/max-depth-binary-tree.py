# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = []
        current = root
        temp = 0
        max_depth = 0

        while current or stack:
            if current:
                temp += 1
                stack.append((current, temp))
                current = current.left
            else:
                max_depth = max(max_depth, temp)
                temp -= 1
                current, temp = stack.pop()
                current = current.right    
        return max_depth