"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:

        res = []
        
        def visit(root):

            if root is None:
                return
            
            for child in root.children:
                visit(child)
            
            res.append(root.val)
        
        visit(root)
        return res