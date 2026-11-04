class Solution(object):
    def insert(self, intervals, newInterval):
        intervals.append(newInterval)
        intervals.sort()
        result = []
        start = intervals[0][0]
        end = intervals[0][1]
        for i in range(1, len(intervals)):
            s = intervals[i][0]
            e = intervals[i][1]
            if s <= end:
                if e > end:
                 end = e
            else:
                result.append([start, end])
                start = s
                end = e
        result.append([start, end])
        return result
