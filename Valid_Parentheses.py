class Solution(object):
    def isValid(self, s):
        pairs = {')': '(', '}': '{', ']': '['}
        stack = []

        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)

        return not stack
