# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        level = 0
        queue = deque()
        if root:
            queue.append(root)
            res.append([root.val])

        while queue:
            nest = []
            for i in range(len(queue)):
                curr = queue.popleft()
                if curr.left:
                    queue.append(curr.left)
                    nest.append(curr.left.val)
                if curr.right:
                    queue.append(curr.right)
                    nest.append(curr.right.val)
            level += 1
            if queue:
                res.append(nest)
        return res 
        
