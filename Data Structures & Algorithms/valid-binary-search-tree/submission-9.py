# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, maxm, minm):
            if not root:
                return True
            check = minm < root.val < maxm
            
            return check and dfs(root.left, root.val, minm) and dfs(root.right, maxm, root.val)
        
        return dfs(root, float("inf"), float("-inf"))
        