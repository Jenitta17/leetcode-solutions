class Solution(object):
    def searchRange(self, nums, target):
        def find(go_left):
            lo, hi = 0, len(nums) - 1
            ans = -1
            while lo <= hi:
                mid = (lo + hi) // 2
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid - 1
                else:
                    ans = mid
                    if go_left:
                        hi = mid - 1
                    else:
                        lo = mid + 1
            return ans

        return [find(True), find(False)]
