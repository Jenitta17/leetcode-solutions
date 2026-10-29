class Solution(object):
    def generateParenthesis(self, n):
        result = []

        def backtrack(current, opens, closes):
            if len(current) == 2 * n:
                result.append(current)
                return
            if opens < n:
                backtrack(current + "(", opens + 1, closes)
            if closes < opens:
                backtrack(current + ")", opens, closes + 1)

        backtrack("", 0, 0)
        return result
