import unittest
from typing import Optional
from trees.max_depth_binary_tree.tree import TreeNode


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_count = self.maxDepth(root.left)
        right_count = self.maxDepth(root.right)
        return max(left_count, right_count) + 1

class TestMethods(unittest.TestCase):

    def test_case1(self):
        self.assertTrue()
