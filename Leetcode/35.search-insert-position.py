#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        a = len(nums)//2
        decrease = False
        increase = False
        if target < nums[0]:
            return 0
        if target > nums[len(nums) - 1]:
            return len(nums)
        while a>=0 and a < len(nums):
            if target == nums[a]:
                return a
            elif target < nums[a]:
                a = a - 1
                if increase:
                    return a + 1
                decrease = True
            elif target > nums[a]:
                a = a + 1
                if decrease:
                    return a
                increase = True
        return a
        pass
# @lc code=end

