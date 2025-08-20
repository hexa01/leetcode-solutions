#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        a = m + n - 1
        m = m - 1
        n = n - 1
        while (m>=0 and n>=0):
            if (nums1[m] > nums2[n]):
                nums1[a] = nums1[m]
                m = m - 1
                
            else:
                nums1[a] = nums2[n]
                n = n - 1 
            a = a - 1
                
        if (n >= 0):
            for i in range(a+1):
                nums1[i] = nums2[i]



        
# @lc code=end

