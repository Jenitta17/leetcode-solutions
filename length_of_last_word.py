class Solution(object):
    def lengthOfLastWord(self, s):
        length = 0
        last = 0
        for c in s:
            if c != ' ':
                length += 1
                last = length
            else:
                length = 0
        return last
