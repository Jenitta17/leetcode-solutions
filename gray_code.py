class Solution(object):
    def grayCode(self, n):
        result = [0]
        for bit in range(n):
            top = 1 << bit
            for i in range(len(result) - 1, -1, -1):
                result.append(result[i] + top)
        return result
