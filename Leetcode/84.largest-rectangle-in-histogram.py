#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        #monotonic stack: O(n)
        stack = [-1]
        for i,h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                area = max(area, height * width)
            stack.append(i)
        n = len(heights)
        while stack[-1] != -1:
            height = heights[stack.pop()]
            width = n - stack[-1] - 1
            area = max(area, height * width)
            
        return area
        
# @lc code=end

