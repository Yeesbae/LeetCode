# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """

        if not root:
            return []

        visited = []
        stack = []

        stack.append(root)

        while stack:
            node = stack.pop()
            visited.append(node.val)

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
            
        visited.reverse()
        return visited
