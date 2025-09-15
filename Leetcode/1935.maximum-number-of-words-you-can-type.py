#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        #daily question: 2025/09/15
        words = text.split(' ')
        count = len(words)
        for word in words:
            for c in word:
                if c in brokenLetters:
                    count -= 1
                    break
        return count
        
# @lc code=end

