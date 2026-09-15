class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxD = 0

        def traverse(node):
            nonlocal maxD  # declare it once, on its own line

            if node is None:
                return 0

            leftHeight = traverse(node.left)
            rightHeight = traverse(node.right)

            maxD = max(maxD, leftHeight + rightHeight)  # now this assignment updates the outer one

            return max(leftHeight, rightHeight) + 1

        traverse(root)
        return maxD