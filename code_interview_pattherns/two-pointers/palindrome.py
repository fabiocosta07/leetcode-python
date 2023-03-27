import unittest
import math


class Solution:
    def is_palindrome(self, s):
        middle = math.floor(len(s) / 2)
        for i in range(middle):
            p1 = i
            p2 = (len(s) - 1) - p1
            if s[p1] != s[p2]:
                return False
        return True

    def is_palindromeV2(self, s):
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True


class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.is_palindrome('kavak')
        self.assertTrue(res)

    def test_case2(self):
        sol = Solution()
        res = sol.is_palindrome("DCBAABCD")
        self.assertTrue(res)

    def test_case1V2(self):
        sol = Solution()
        res = sol.is_palindromeV2('kavak')
        self.assertTrue(res)

    def test_case2V2(self):
        sol = Solution()
        res = sol.is_palindromeV2("DCBAABCD")
        self.assertTrue(res)
