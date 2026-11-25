class Solution(object):
    def sortedListToBST(self, head):
        nums = []
        current = head
        while current is not None:
            nums.append(current.val)
            current = current.next
        def build(low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            node.left = build(low, mid - 1)
            node.right = build(mid + 1, high)
            return node
        return build(0, len(nums) - 1)
