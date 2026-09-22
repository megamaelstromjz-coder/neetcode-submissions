# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def depth(root):

            if root is None:
                return 0

            left = depth(root.left)
            if left == -1:
                return -1
            right = depth(root.right)
            if right == -1:
                return -1

            if abs(left-right) > 1:
                return -1
            else:
                return max(left+1,right+1)
            
        return depth(root) != -1 

            
        

