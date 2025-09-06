#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0

        #brute force: O(n^2)
        for i in range(len(heights)):
            height = heights[i]
            left = i
            right = i
            while left > 0 and heights[left -1] >= height:
                left -= 1 
            while right < len(heights)-1  and heights[right +1] >= height:
                right += 1 
            width = right - left + 1
            area = max(area, width * height)
        return area
        
# @lc code=end

