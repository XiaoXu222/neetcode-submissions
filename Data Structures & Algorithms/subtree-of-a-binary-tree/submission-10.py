# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSameTree(p, q):
            if (not p) and (not q):
                return True
            elif ((not p) and q) or ((not q) and p):
                return False
            
            return p.val == q.val and isSameTree(q.left, p.left) and isSameTree(q.right, p.right)
        
            
        if not root:
            return False
        check = isSameTree(root, subRoot)
        return check or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot) 

    
        
            
        
            
        
        