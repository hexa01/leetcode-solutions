#
# @lc app=leetcode id=643 lang=python3
#
# [643] Maximum Average Subarray I
#

# @lc code=start
class Solution:
    def findMaxAverage(self, nums: list[int], k: int) -> float:
        curr_sum = sum(nums[:k])
        max_avg = curr_sum / k
        for i in range(len(nums)-k):
            curr_sum = curr_sum - nums[i] + nums[i+k]
            curr_avg = curr_sum / k
            max_avg = max(curr_avg,max_avg)
        return max_avg
        
        
# @lc code=end

