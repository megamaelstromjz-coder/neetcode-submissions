# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    def mDepth(self, root, c):

            if root is None:
                return c
            
            lDepth = self.mDepth(root.right, c+1)
            rDepth = self.mDepth(root.left, c+1)

            return max(lDepth, rDepth)

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        return self.mDepth(root, 0)
