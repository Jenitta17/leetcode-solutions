class Solution(object):
    def isBalanced(self, root):
        def height(node):
            if node is None:
                return 0
            left_h = height(node.left)
            right_h = height(node.right)
            if left_h > right_h:
                return left_h + 1
            else:
                return right_h + 1
        if root is None:
            return True
        diff = height(root.left) - height(root.right)
        if diff > 1 or diff < -1:
            return False
        return self.isBalanced(root.left) and self.isBalanced(root.right)
