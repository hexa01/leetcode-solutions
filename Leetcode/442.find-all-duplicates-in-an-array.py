#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        for num in nums:
            abs_num = abs(num)
            if nums[abs_num - 1] < 0:
                duplicates.append(abs_num)
            else:
                nums[abs_num - 1] = -nums[abs_num - 1]
        return duplicates
        
# @lc code=end

