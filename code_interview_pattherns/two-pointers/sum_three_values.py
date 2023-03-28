import unittest


class Solution:
    def find_sum_of_three(self, nums, target):
        nums.sort()

        for i in range(len(nums)):
            p1 = i + 1
            p2 = len(nums) - 1

            while p1 < p2:
                three_sum = nums[i] + nums[p1] + nums[p2]
                if three_sum == target:
                    return True
                if three_sum > target:
                    p2 -= 1
                else:
                    p1 += 1
        return False


class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.find_sum_of_three([3, 7, 1, 2, 8, 4, 5], 10)
        self.assertTrue(res)


    def test_case1(self):
        sol = Solution()
        res = sol.find_sum_of_three([1, -1, 0] , -1)
        self.assertFalse(res)
