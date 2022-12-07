import unittest
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None:
            return False
        pathMap = {}
        nextNode = head
        while nextNode.next != None:
            if nextNode in pathMap:
                return True
            pathMap[nextNode] = True
            nextNode = nextNode.next
        return False




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
