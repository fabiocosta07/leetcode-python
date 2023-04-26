import unittest
import math


class Solution:
    def is_happy_humber(self, n):
        slow = n
        fast = self.sum_of_squared_digits(n)

        while fast != 1 and slow != fast:
            slow = self.sum_of_squared_digits(slow)
            fast = self.sum_of_squared_digits(self.sum_of_squared_digits(fast))

        if fast == 1:
            return True

        return False

    def sum_of_squared_digits(self, number): # Helper function that calculates the sum of squared digits.
        total_sum = 0
        while number > 0:
            digit = number % 10
            number = number // 10
            total_sum += digit ** 2
        return total_sum
class TestMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.is_happy_humber(28)
        self.assertTrue(res)
