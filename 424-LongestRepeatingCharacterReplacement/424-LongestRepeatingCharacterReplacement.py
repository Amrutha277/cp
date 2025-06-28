# Last updated: 6/28/2025, 12:14:07 AM
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp_set= set(s)
        length=0
        for char in temp_set:
            count=0
            l=0
            for r in range(len(s)):
                if s[r]== char:
                    count+=1
                while (r-l+1)- count >k:
                    if s[l]== char:
                        count-=1    
                    l+=1
                
                length= max(length, r-l+1)
        return length