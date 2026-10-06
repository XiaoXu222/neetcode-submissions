# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(root, sumV):
            if not root:
                return False
            sumV += root.val

            if sumV == targetSum and not root.left and not root.right:
                return True

            if dfs(root.left, sumV):
                return True
            if dfs(root.right, sumV):
                return True
            sumV -= root.val
            return False
        return dfs(root, 0)
        


        