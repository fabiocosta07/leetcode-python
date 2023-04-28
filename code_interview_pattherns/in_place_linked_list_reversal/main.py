import unittest

from linked_list import LinkedList
from utils.leetcode_utils import compare_linked_list


class Solution:
    def reverse(self, head):
        curr_node = head
        prev = None
        while curr_node:
            if not curr_node.next:
                head = curr_node
            next_node = curr_node.next
            curr_node.next = prev
            prev = curr_node
            curr_node = next_node
        return head

class TestMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        ll = LinkedList()
        ll.create_linked_list([1, -2, 3, 4, -5, 4, 3, -2, 1])
        res = sol.reverse(ll.head)
        llcompare = LinkedList()
        llcompare.create_linked_list([1, -2, 3, 4, -5, 4, 3, -2, 1])
        self.assertTrue(compare_linked_list(llcompare.head, res))
