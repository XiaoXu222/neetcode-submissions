# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root, minVal, maxVal):

            if not root:
                return True
            if minVal < root.val < maxVal:
                nodeCheck = True
            else:
                nodeCheck = False
            leftCheck = dfs(root.left, minVal, root.val)
            rightCheck = dfs(root.right, root.val, maxVal)
            return (nodeCheck and leftCheck and rightCheck)
        return dfs(root, float("-inf"), float("+inf"))
            
            