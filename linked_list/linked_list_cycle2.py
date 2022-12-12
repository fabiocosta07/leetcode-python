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

    def detectCycle_sol2(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        next_node_slow = head
        next_node_fast = head
        while next_node_slow \
                and next_node_fast \
                and next_node_fast.next:
            next_node_slow = next_node_slow.next
            next_node_fast = next_node_fast.next.next
            if next_node_fast is next_node_slow:
                return next_node_fast
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

    def test_case1_sol2(self):
        sol = Solution()
        res = sol.detectCycle_sol2(build_input_list([3, 2, 0, -4], 1))
        self.assertTrue(res)

    def test_case2_sol2(self):
        sol = Solution()
        res = sol.detectCycle_sol2(build_input_list([1, 2], 0))
        self.assertTrue(res)

    def test_case3_sol2(self):
        sol = Solution()
        res = sol.detectCycle_sol2(build_input_list([1], -1))
        self.assertFalse(res)


if __name__ == '__main__':
    unittest.main()

# time complexity 0(2n) => O(n)
# space complexity ?
