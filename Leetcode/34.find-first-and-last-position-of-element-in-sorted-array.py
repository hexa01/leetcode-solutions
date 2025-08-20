#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        def findIndex(target):
            a, b = 0, len(nums)
            while a<b:
                m = (a + b) // 2
                if nums[m] < target:
                    a = m + 1
                else:
                    b = m
            return a

        first = findIndex(target)
        if first == len(nums) or nums[first] != target:
            return [-1,-1]
        last = findIndex(target + 1) - 1
        return [first,last]
        
# @lc code=end

