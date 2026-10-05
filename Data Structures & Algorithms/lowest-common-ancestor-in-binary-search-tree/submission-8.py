# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        res = None

        def dfs(root, p, q):
            nonlocal res
            if not root:
                return 0
            if root == p or root == q:
                number = 1 + dfs(root.left, p, q) + dfs(root.right, p, q)
            else:
                number = dfs(root.left, p, q) + dfs(root.right, p, q)
            if number == 2 and res == None:
                res = root
            return number
        
        dfs(root, p, q)
        return res
        