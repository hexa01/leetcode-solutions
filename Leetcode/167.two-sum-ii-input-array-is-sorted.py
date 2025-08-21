#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input Array Is Sorted
#

# @lc code=start
class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        a, b = 0, len(numbers) - 1
        while a < b:
            sum = numbers[a] + numbers[b]
            if sum == target:
                return [a + 1, b + 1]
            elif sum < target:
                a += 1
            else:
                b -= 1
        
        
# @lc code=end

