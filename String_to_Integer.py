class Solution(object):
    def myAtoi(self, s):
        i, n = 0, len(s)
        while i < n and s[i] == ' ':
            i += 1

        sign = 1
        if i < n and s[i] in '+-':
            if s[i] == '-':
                sign = -1
            i += 1

        result = 0
        while i < n and '0' <= s[i] <= '9':
            result = result * 10 + (ord(s[i]) - ord('0'))
            i += 1

        result *= sign
        if result > 2**31 - 1:
            return 2**31 - 1
        if result < -2**31:
            return -2**31
        return result
