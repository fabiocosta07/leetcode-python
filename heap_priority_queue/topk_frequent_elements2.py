import unittest
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # HashMap to store count of the elements
        count = {}
        for n in nums:
            count[n] = count.get(n, 0) + 1

        # Array to store the elements according
        # to their frequency
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in count.items():
            freq[c].append(n)

        res = []
        # if K elements have been printed
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res


class TestMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.topKFrequent([1, 1, 1, 2, 2, 3], 2)
        self.assertIn(res, [[1, 2], [2, 1]])

    def test_case2(self):
        sol = Solution()
        res = sol.topKFrequent([1], 1)
        self.assertIn(res, [[1]])

    def test_case3(self):
        sol = Solution()
        res = sol.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2)
        self.assertIn(res, [[-1, 2]])


if __name__ == '__main__':
    unittest.main()
