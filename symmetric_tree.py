class Solution(object):
    def isSymmetric(self, root):
        def is_mirror(a, b):
            if a is None and b is None:
                return True
            if a is None or b is None:
                return False
            if a.val != b.val:
                return False
            outer = is_mirror(a.left, b.right)
            inner = is_mirror(a.right, b.left)
            return outer and inner
        return is_mirror(root.left, root.right)
