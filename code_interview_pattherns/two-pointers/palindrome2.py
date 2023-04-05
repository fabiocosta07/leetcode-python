import unittest


class Solution:
    def is_palindrome_problem2(self, s):
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            if s[p1] != s[p2]:
                if not (self.is_palindrome_check(s[p1 + 1:p2 + 1]) or
                        self.is_palindrome_check(s[p1:p2])):
                    return False
            p1 += 1
            p2 -= 1
        return True

    def is_palindrome_check(self, s):
        p1 = 0
        p2 = len(s) - 1
        while p1 <= p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        return True


class TestStringMethods(unittest.TestCase):

    def test_case(self):
        sol = Solution()
        res = sol.is_palindrome_problem2('madame')
        self.assertTrue(res)

    def test_case2(self):
        sol = Solution()
        res = sol.is_palindrome_problem2('eeccccbebaeeabebccceea')
        self.assertFalse(res)

    def test_case3(self):
        sol = Solution()
        res = sol.is_palindrome_problem2('tebbem')
        self.assertFalse(res)
