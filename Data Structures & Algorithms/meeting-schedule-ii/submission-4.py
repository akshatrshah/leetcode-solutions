"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if len(intervals) == 0:
            return 0
        res = 1

        heap = []

        intervals.sort(key=lambda x:x.start)

        for i in range(len(intervals)):
            print(heap)
            while heap and heap[0] <= intervals[i].start:
                heapq.heappop(heap)
            else:
                heapq.heappush(heap,intervals[i].end)
                res = max(res,len(heap))
        return res


