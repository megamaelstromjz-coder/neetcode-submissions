# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def bal(root):
            if root is None:
                return 0
            
            x = bal(root.left)
            if x == -1:
                return -1
            y = bal(root.right)
            if y == -1:
                return -1

            if abs(x-y) > 1:
                return -1
                
            
            return max(x,y) + 1

        return bal(root) != -1