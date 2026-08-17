# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        largest = root.val

        def dfs(node):
            nonlocal largest

            if node == None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right) 

            
            res = max(max(0, left) + node.val, max(0, right) + node.val)
            largest = max(largest, res, left + right + node.val)
            
            return res
        
        dfs(root)
        return largest