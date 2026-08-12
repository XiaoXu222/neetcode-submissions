# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False
        
        def dfs(root, subRoot):
            if not root and not subRoot:
                return True
            if root and subRoot and root.val == subRoot.val:
                return dfs(root.left, subRoot.left) and dfs(root.right, subRoot.right)
            else:
                return False
        
        def dfs2(root, subRoot):
            nonlocal res
            if not root:
                return 
            if root and subRoot and root.val == subRoot.val:
                if dfs(root, subRoot):
                    res = True
            dfs2(root.left, subRoot)
            dfs2(root.right, subRoot)
        
        dfs2(root, subRoot)
        return res



        
        
        
        