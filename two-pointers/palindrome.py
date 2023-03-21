import unittest
import math

class Solution:
    def is_palindrome(self, s):
        # Write your code here
        # Tip: You may use the code template provided
        # in the two_pointers.py file
        middle = math.floor(len(s) / 2)
        p2 = len(s) - 1
        for i in range(middle):
            p1 = i
            p2 -= p1
            if s[p1] != s[p2]:
                return False
        return True

class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.is_palindrome('kavak')
        self.assertTrue(res)