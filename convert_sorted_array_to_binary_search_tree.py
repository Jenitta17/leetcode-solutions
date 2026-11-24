class Solution(object):
    def sortedArrayToBST(self, nums):
        def build(low, high):
            if low > high:
                return None
            mid = (low + high) // 2
            node = TreeNode(nums[mid])
            node.left = build(low, mid - 1)
            node.right = build(mid + 1, high)
            return node
        return build(0, len(nums) - 1)
