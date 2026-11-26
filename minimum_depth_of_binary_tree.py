class Solution(object):
    def minDepth(self, root):
        if root is None:
            return 0
        if root.left is None:
            return self.minDepth(root.right) + 1
        if root.right is None:
            return self.minDepth(root.left) + 1
        left_depth = self.minDepth(root.left)
        right_depth = self.minDepth(root.right)
        if left_depth < right_depth:
            return left_depth + 1
        else:
            return right_depth + 1
