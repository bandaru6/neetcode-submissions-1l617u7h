"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        count = res = 0
        s = e = 0

        while e < len(end):
            if s < len(start) and start[s] < end[e]:
                count += 1
                s += 1
            else:
                res = max(res, count)
                count -= 1
                e += 1

        return res
