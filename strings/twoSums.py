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
            dictNums[nums[n]] = n
        for n in range(0, len(nums)):
            diff = target - nums[n]
            if diff in dictNums and n != dictNums[diff]:
                return [n, dictNums[diff]]
        return []

class TestStringMethods(unittest.TestCase):

    def test_case1(self):
        sol = Solution()
        res = sol.twoSum([2,7,11,15], 9)
        self.assertEqual([0,1], res)

    def test_case2(self):
        sol = Solution()
        res = sol.twoSum([3,2,4], 6)
        self.assertEqual([1,2], res)

    def test_case3(self):
        sol = Solution()
        res = sol.twoSum([3,3], 6)
        self.assertEqual([0,1], res)

if __name__ == '__main__':
    unittest.main()

#time complexity 0(2n) => O(n)
#space complexity ?