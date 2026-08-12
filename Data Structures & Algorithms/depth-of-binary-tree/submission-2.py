# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        # 第一步：专门派人去查左子树的最大深度（问左边的 VP）
        left_depth = self.maxDepth(root.left)
        
        # 第二步：专门派人去查右子树的最大深度（问右边的 VP）
        right_depth = self.maxDepth(root.right)

        depth = 1 + max(left_depth, right_depth)
        
        # 第三步：无情对比，挑出最大的那一个，加上自己这 1 层，向上汇报
        return depth
        # level = 0
        # if not root:
        #     return level
        # queue = deque([root])
        # while queue:
        #     for i in range(len(queue)):
        #         node = queue.popleft()
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     level += 1
        # return level
    
        
        