class Solution(object):
    def permuteUnique(self, nums):
        result = [[]]
        for x in nums:
            new_result = []
            for p in result:
                for i in range(len(p) + 1):
                    new_result.append(p[:i] + [x] + p[i:])
            result = new_result
        unique = []
        for p in result:
            if p not in unique:
                unique.append(p)
        return unique
