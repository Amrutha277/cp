# Last updated: 6/27/2025, 4:33:05 PM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp= set()
        l=0
        maxl=0
        for r in range(len(s)):
            while s[r] in temp:
                temp.remove(s[l])
                l+=1
            temp.add(s[r])
            maxl= max(maxl, r-l+1)
        return maxl

        

