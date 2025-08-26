#
# @lc app=leetcode id=2090 lang=python3
#
# [2090] K Radius Subarray Averages
#

# @lc code=start
class Solution:
    def getAverages(self, nums: list[int], k: int) -> list[int]:
        prefix_sum = []
        n = len(nums)
        op = [-1 for i in range(n)]
        prefix_sum.append(nums[0])
        for i in range(1,n):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])
        
        a = 0
        b = 0
        for i in range(n):
            if i - k >= 0 and i + k <= n - 1:
                op[i] = (prefix_sum[i+k] - b)// (2*k + 1)
                if a <= n-1:
                    b = prefix_sum[a] 
                a += 1

        return op

# @lc code=end

