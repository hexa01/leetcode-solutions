#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        a = len(digits) - 1
        while a >= 0:
            if digits[a] == 9:
                digits[a] = 0
                a -= 1
            else:
                digits[a] = digits[a] + 1
                return digits
        digits.insert(0,1)
        return digits
        pass
        
# @lc code=end

