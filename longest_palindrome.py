class Solution(object):
    def longestPalindrome(self, s):
        start, end = 0, 0

        def expand(lo, hi):
            while lo >= 0 and hi < len(s) and s[lo] == s[hi]:
                lo -= 1
                hi += 1
            return lo + 1, hi - 1

        for i in range(len(s)):
            for lo, hi in (expand(i, i), expand(i, i + 1)):
                if hi - lo > end - start:
                    start, end = lo, hi

        return s[start:end + 1]
