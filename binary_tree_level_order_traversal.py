class Solution(object):
    def levelOrder(self, root):
        if root is None:
            return []
        result = []
        queue = [root]
        while len(queue) > 0:
            level_size = len(queue)
            level = []
            for i in range(level_size):
                node = queue.pop(0)
                level.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level)
        return result
