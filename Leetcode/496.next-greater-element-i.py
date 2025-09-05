#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        mapping = {}
        stack = []
        for _ in range(len(nums2)):
            while stack and nums2[_] > nums2[stack[-1]]:
                mapping[nums2[stack.pop()]] = nums2[_]
            stack.append(_) 
        for _ in range(len(nums1)):
            ans.append(mapping.get(nums1[_], -1))
        return ans
        
# @lc code=end

