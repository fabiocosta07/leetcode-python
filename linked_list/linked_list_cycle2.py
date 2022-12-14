import unittest
from typing import Optional

from utils.leetcode_utils import build_input_list, ListNode, get_linked_list_cycle_node


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
            return None
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
        pos = 1
        input_list = build_input_list([3, 2, 0, -4], pos)
        sol = Solution()
        res = sol.detectCycle(input_list)
        expected = get_linked_list_cycle_node(input_list, pos)
        self.assertEqual(res, expected)

    def test_case2(self):
        pos = 0
        input_list = build_input_list([1, 2], pos)
        sol = Solution()
        res = sol.detectCycle(input_list)
        expected = get_linked_list_cycle_node(input_list, pos)
        self.assertEqual(expected, res)

    def test_case3(self):
        pos = -1
        input_list = build_input_list([1], pos)
        sol = Solution()
        res = sol.detectCycle(input_list)
        expected = get_linked_list_cycle_node(input_list, pos)
        self.assertEqual(expected, res)

    def test_case1_sol2(self):
        pos = 1
        input_list = build_input_list([3, 2, 0, -4], pos)
        sol = Solution()
        res = sol.detectCycle(input_list)
        expected = get_linked_list_cycle_node(input_list, pos)
        self.assertEqual(res, expected)


    def test_case2_sol2(self):
        pos = 0
        input_list = build_input_list([1, 2], pos)
        sol = Solution()
        res = sol.detectCycle(input_list)
        expected = get_linked_list_cycle_node(input_list, pos)
        self.assertEqual(expected, res)

    def test_case3_sol2(self):
        pos = -1
        input_list = build_input_list([1], pos)
        sol = Solution()
        res = sol.detectCycle(input_list)
        expected = get_linked_list_cycle_node(input_list, pos)
        self.assertEqual(expected, res)


if __name__ == '__main__':
    unittest.main()

# time complexity 0(2n) => O(n)
# space complexity ?
