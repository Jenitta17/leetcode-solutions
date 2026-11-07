class Solution(object):
    def mySqrt(self, x):
        low = 0
        high = x
        answer = 0
        while low <= high:
            mid = (low + high) // 2
            if mid * mid <= x:
                answer = mid
                low = mid + 1
            else:
                high = mid - 1
        return answer
