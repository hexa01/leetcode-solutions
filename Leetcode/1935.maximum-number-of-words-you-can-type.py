#
# @lc app=leetcode id=1935 lang=python3
#
# [1935] Maximum Number of Words You Can Type
#

# @lc code=start
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        #daily question: 2025/09/15
        broken_set = set(brokenLetters)
        #python one liner: equivalent to this
        # count = 0
        # for word in text.split():
        #     if all(c not in broken_set for c in word):
        #     count += 1
        # return count
        return sum(all(c not in broken_set for c in word) for word in text.split())
        
# @lc code=end

