#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        direction = 0 
        for i in range(1,n):
            if nums[i] > nums[i-1]: 
                if direction < 0:
                    return False
                direction = 1

            if nums[i] < nums[i-1]:
                if direction > 0:
                    return False
                direction = -1
        return True
        
# @lc code=end

