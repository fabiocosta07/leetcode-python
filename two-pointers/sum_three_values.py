import unittest


class Solution:
    def find_sum_of_three(self, nums, target):
        s_nums = nums.sort()

        p1 = 0
        p2 = len(s_nums) - 1

        for i in range(len(s_nums)):
            return False


class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.find_sum_of_three([3, 7, 1, 2, 8, 4, 5], 10)
        self.assertTrue(res)
