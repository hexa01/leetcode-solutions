#
# @lc app=leetcode id=76 lang=python3
#
# [76] Minimum Window Substring
#

# @lc code=start
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        window,countT = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        have, need = 0, len(countT)
        res = [-1,-1]
        resLen = len(s) + 1
        left = 0
        for right in range(len(s)):
            c = s[right]
            window[c] = window.get(c, 0) + 1
            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (right -  left + 1) < resLen:
                    res = [left,right]
                    resLen = right - left + 1
                window[s[left]] -= 1
                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1
                left += 1
        
        return s[res[0]: res[1] + 1] if (resLen < len(s) + 1) else ""
        
# @lc code=end

