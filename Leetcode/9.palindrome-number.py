#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):  #eliminates -ve and num>0 ending with 0.
            return False
        reversed_num = 0
        num = x
        while(num > 0):
            reversed_num = reversed_num * 10 + num % 10
            num = num // 10
        return x == reversed_num
        pass
# @lc code=end

