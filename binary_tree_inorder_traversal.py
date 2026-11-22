class Solution(object):
    def inorderTraversal(self, root):
        result = []
        def visit(node):
            if node is None:
                return
            visit(node.left)
            result.append(node.val)
            visit(node.right)
        visit(root)
        return result
