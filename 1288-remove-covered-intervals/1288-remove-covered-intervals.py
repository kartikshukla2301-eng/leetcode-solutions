class Solution:
    def removeCoveredIntervals(self, intervals):
        intervals.sort(key=lambda x: (x[0], -x[1]))

        ans = 0
        max_end = 0

        for _, end in intervals:
            if end > max_end:
                ans += 1
                max_end = end

        return ans