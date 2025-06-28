# Last updated: 6/28/2025, 12:30:06 AM
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pf= Counter(p)
        len_p = len(p)
        res=[]

        for l in range(len(s) - len_p + 1):
            window = s[l:l + len_p]
            if Counter(window)== pf:
                res.append(l)
        return res