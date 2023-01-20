import unittest
from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        window = deque()
        window_size = k
        if len(nums) == 0:
            return result

        if k > len(nums):
            window_size = len(nums)

        for i in range(window_size):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            window.append(i)
        result.append(nums[window[0]])
        for i in range(window_size, len(nums)):
            while window and nums[i] >= nums[window[-1]]:
                window.pop()
            while window and window[0] <= (i - window_size):
                window.popleft()
            window.append(i)
            result.append(nums[window[0]])
        return result


class TestMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3)
        self.assertEqual([3, 3, 5, 5, 6, 7], res)

    def test_case2(self):
        sol = Solution()
        res = sol.maxSlidingWindow([7, 2, 4], 2)
        self.assertEqual([7, 4], res)
