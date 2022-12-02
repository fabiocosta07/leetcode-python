import unittest


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        open_chars = ['(', '[', '{']
        stack = []
        for i in range(0, len(s)):
            if s[i] in open_chars:
                stack.append(s[i])
            elif len(stack) > 0:
                last = stack.pop()
                if s[i] == ')' and last != '(':
                    return False
                elif s[i] == ']' and last != '[':
                    return False
                elif s[i] == '}' and last != '{':
                    return False
            else:
                return False
        if len(stack) != 0:
            return False
        return True
class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.isValid("()")
        self.assertTrue(res)

    def test_case2(self):
        sol = Solution()
        res = sol.isValid("()[]{}")
        self.assertTrue(res)

    def test_case3(self):
        sol = Solution()
        res = sol.isValid("(]")
        self.assertFalse(res)

    def test_case4(self):
        sol = Solution()
        res = sol.isValid("]")
        self.assertFalse(res)

if __name__ == '__main__':
    unittest.main()

# time complexity 0(2n) => O(n)
# space complexity ?
