# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        indexMap = {}
        for i, value in enumerate(inorder):
            indexMap[value] = i
        preIndex = 0

        def dfs(l, r):  
            nonlocal preIndex
                
            if l > r:
                return None

            rootValue = preorder[preIndex]
            root = TreeNode(rootValue)
            preIndex += 1

            mid = indexMap[root.val]
            root.left = dfs(l, mid-1)
            root.right = dfs(mid+1, r)
            return root

        return dfs(0, len(preorder) - 1)




    
        