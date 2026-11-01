class Solution(object):
    def combinationSum(self, candidates, target):
        result = []
        def backtrack(start, remaining, current):
            if remaining == 0:
                result.append(current[:])
                return
            for i in range(start, len(candidates)):
                if candidates[i] > remaining:
                    continue
                current.append(candidates[i])
                backtrack(i, remaining - candidates[i], current)
                current.pop()
        backtrack(0, target, [])
        return result
