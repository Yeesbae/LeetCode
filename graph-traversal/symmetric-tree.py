# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        stack = []
        left = root.left
        right = root.right

        while left or right or stack:
            if left and right:
                if left.val != right.val:
                    return False
                stack.append((left, right))
                left = left.left
                right = right.right
            else:
                if not left and right or left and not right:
                    return False
                left, right = stack.pop()
                left = left.right
                right = right.left
        return True

        


        