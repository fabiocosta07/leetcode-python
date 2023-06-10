import unittest
from typing import Optional
from trees.max_depth_binary_tree.tree import TreeNode


class Solution:

    def isValidBST2(self, root: Optional[TreeNode]) -> bool:
        INT_MAX = 4294967296
        INT_MIN = -4294967296
        return self.traversal2(root, INT_MIN, INT_MAX)

    def traversal2(self, node: Optional[TreeNode], min: int, max: int) -> bool:
        left_is_valid = True
        right_is_valid = True
        current_is_valid = min < node.val < max
        if node.left:
            left_is_valid = self.traversal2(node.left, min, node.val)
        if node.right:
            right_is_valid = self.traversal2(node.right, node.val, max)
        return current_is_valid and left_is_valid and right_is_valid

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.seq = []
        self.traversal(root)
        for i in range(1, len(self.seq)):
            if not self.seq[i - 1] < self.seq[i]:
                return False
        return True


    def traversal(self, node: Optional[TreeNode]):
        if node.left:
            self.traversal(node.left)
        self.seq.append(node.val)
        if node.right:
            self.traversal(node.right)


class TestMethods(unittest.TestCase):

    def test_case1(self):
        self.assertTrue()
