class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]

        for i in range(n - 2):
            lo, hi = i + 1, n - 1
            while lo < hi:
                total = nums[i] + nums[lo] + nums[hi]

                if abs(total - target) < abs(closest - target):
                    closest = total

                if total < target:
                    lo += 1
                elif total > target:
                    hi -= 1
                else:
                    return total

        return closest
