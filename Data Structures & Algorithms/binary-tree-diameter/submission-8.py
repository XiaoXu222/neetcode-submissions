# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue = deque()
        def dfs(root,queue):
            if not root:
                return 0          
            leftL = dfs(root.left,queue)
            rightL = dfs(root.right,queue)
            queue.append(leftL+rightL)
            return 1 + max(leftL, rightL)
        
        dfs(root,queue)
        res = max(queue)
        return res
        