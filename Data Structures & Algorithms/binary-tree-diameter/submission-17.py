# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # res = 0
    
        def dfs(root):
            # nonlocal res

            if not root:
                return [0, 0]   

            leftL = dfs(root.left)
            rightL = dfs(root.right)

            length = max(leftL[0], rightL[0], leftL[1] + rightL[1])

            return [length, 1 + max(leftL[1], rightL[1])]
        
        

        return dfs(root)[0]
        # res = [0]

        # def dfs(root,res):
        #     if not root:
        #         return 0          
        #     leftL = dfs(root.left,res)
        #     rightL = dfs(root.right,res)
        #     res[0] = max(res[0], leftL + rightL)
        #     return 1 + max(leftL, rightL)
        
        # dfs(root,res)
        # return res[0]
        