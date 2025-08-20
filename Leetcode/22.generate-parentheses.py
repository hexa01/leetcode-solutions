#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        finalResult = []
        def helper(o,c,result,finalResult):
            if o == 0 and c == 0:
                finalResult.append(result)
                return
            if o != 0:
                helper(o -1, c, result + "(", finalResult)
            if c > o:
                helper(o, c-1, result + ")", finalResult)
        
        helper(n,n,"",finalResult)
        return finalResult
        
# @lc code=end

