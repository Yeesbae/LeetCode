# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: bool
        """
        if not root:
            return False

        visited = []
        stack = []
        result = []

        stack.append((root, root.val))

        while stack:
            node, value = stack.pop()
            visited.append(node)

            if not node.left and not node.right:
                if targetSum == value:
                    return True

            if node.right:
                stack.append((node.right, value + node.right.val))
            if node.left:
                stack.append((node.left, value + node.left.val))
            
        return False

