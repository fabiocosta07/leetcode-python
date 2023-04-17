import unittest
from interval import *



class Solution:
    def merge_intervals(self, intervals):
        if not intervals:
            return None
        result = [Interval(intervals[0].start, intervals[0].end)]
        for i in range(1, len(intervals)):
            last_index = len(result) - 1

            prev_start = result[last_index].start
            prev_end = result[last_index].end

            start = intervals[i].start
            end = intervals[i].end
            if self.is_between(start, prev_start, prev_end):
                if not self.is_between(end, prev_start, prev_end):
                    result[last_index].end = max(end, prev_end)
            else:
                result.append(Interval(start, end))
        return result
    def is_between(self, num, start, end):
        return start <= num <= end


class TestMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        v1 = [Interval(1, 5), Interval(3, 7), Interval(4, 6)]
        res = sol.merge_intervals(v1)
        self.assertListEqual([Interval(1, 7)], res)
