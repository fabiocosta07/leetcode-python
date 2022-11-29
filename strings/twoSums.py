import unittest


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictNums = {}
        for n in range(0, len(nums)):
            diff = target - nums[n]
            if diff in dictNums:
                return [n, dictNums[diff]]
            else:
                dictNums[nums[n]] = n

        return []


class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.twoSum([2, 7, 11, 15], 9)
        self.assertIn(res, [[0, 1], [1, 0]])

    def test_case2(self):
        sol = Solution()
        res = sol.twoSum([3, 2, 4], 6)
        self.assertIn(res, [[1, 2], [2, 1]])

    def test_case3(self):
        sol = Solution()
        res = sol.twoSum([3, 3], 6)
        self.assertIn(res, [[0, 1], [1, 0]])


if __name__ == '__main__':
    unittest.main()

# time complexity 0(2n) => O(n)
# space complexity ?
