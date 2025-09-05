#
# @lc app=leetcode id=496 lang=python3
#
# [496] Next Greater Element I
#

# @lc code=start
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            check = False
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    check  = True
                if check == True and nums2[j] > nums1[i]:
                    ans[i] = nums2[j]
                    break
        return ans
        
# @lc code=end

