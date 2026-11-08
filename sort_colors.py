class Solution(object):
    def sortColors(self, nums):
        count0 = 0
        count1 = 0
        count2 = 0
        for x in nums:
            if x == 0:
                count0 = count0 + 1
            elif x == 1:
                count1 = count1 + 1
            else:
                count2 = count2 + 1
        i = 0
        for a in range(count0):
            nums[i] = 0
            i = i + 1
        for a in range(count1):
            nums[i] = 1
            i = i + 1
        for a in range(count2):
            nums[i] = 2
            i = i + 1
