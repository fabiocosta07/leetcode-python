import unittest
from typing import Optional

from utils.leetcode_utils import build_input_list, ListNode


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        pathMap = {}
        nextNode = head
        while nextNode.next != None:
            if nextNode in pathMap:
                return pathMap[nextNode]
            pathMap[nextNode] = nextNode
            nextNode = nextNode.next
        return None

class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.detectCycle(build_input_list([3, 2, 0, -4], 1))
        self.assertTrue(res)

    def test_case2(self):
        sol = Solution()
        res = sol.detectCycle(build_input_list([1, 2], 0))
        self.assertTrue(res)

    def test_case3(self):
        sol = Solution()
        res = sol.detectCycle(build_input_list([1], -1))
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()

# time complexity 0(2n) => O(n)
# space complexity ?
