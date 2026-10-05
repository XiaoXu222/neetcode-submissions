# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        val2ind = {}
        for i, val in enumerate(inorder):
            val2ind[val] = i
        preInd = 0
        def dfs(l, r):
            nonlocal preInd

            if l > r:
                return None

            preVal = preorder[preInd]
            
            rootNode = TreeNode(preVal)
            preInd += 1
            rootNode.left = dfs(l, val2ind[preVal] - 1)
            rootNode.right = dfs(val2ind[preVal] + 1, r)
            
            

            return rootNode
        return dfs(0, len(preorder) - 1)

        