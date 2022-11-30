import unittest
from typing import List
from queue import PriorityQueue


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter:
                counter[n] = 0
            counter[n] += 1

        pq = PriorityQueue()
        for n in nums:
            pq.put((-counter[n], n))

        res = set()
        for i in range(0, len(nums)):
            res.add(pq.get()[1])
        return list(res)[0: k]


class TestMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
        self.assertIn(res, [[1, 2], [2, 1]])

    def test_case2(self):
        sol = Solution()
        res = sol.topKFrequent([1], 1)
        self.assertIn(res, [[1]])


if __name__ == '__main__':
    unittest.main()
