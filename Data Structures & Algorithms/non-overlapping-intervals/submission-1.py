class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        total = 0
        newIntervals = sorted(intervals, key = lambda x: x[0])
        prevEnd = newIntervals[0][1]

        for i in range(1,len(intervals)):
            current = newIntervals[i]
            if prevEnd > current[0]:
                prevEnd = min(prevEnd, current[1])
                total += 1
            else:
                prevEnd = current[1]
        return total
