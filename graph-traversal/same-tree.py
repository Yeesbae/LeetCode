# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        visited = []
        stack = []
        count = 0
        while p or q or stack:
            if (p and q):
                if p.val != q.val:
                    return False
                stack.append((p, q))
                p = p.left
                q = q.left
            else:
                if (not p and q) or (p and not q):
                    return False
                p, q = stack.pop()
                visited.append((p, q))
                p = p.right
                q = q.right
        return True
            
