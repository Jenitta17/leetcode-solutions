class Solution(object):
    def subsets(self, nums):
        result = [[]]
        for x in nums:
            new_subsets = []
            for s in result:
                new_subsets.append(s + [x])
            result = result + new_subsets
        return result
