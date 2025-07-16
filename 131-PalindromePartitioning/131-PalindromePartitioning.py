# Last updated: 7/15/2025, 8:05:57 PM
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result=[]
        path=[]

        def helper(index, path):
            if index== len(s):
                result.append(path[:])
                return

            for i in range(index, len(s)):
                if ispalindrome(s, index, i):
                    path.append(s[index:i+1])
                    helper(i+1, path)
                    path.pop()

            
        def ispalindrome(s, start, end):
            while start<= end:
                if s[start] != s[end]:
                    return False  
                start+=1
                end-=1
            return True
    
        helper(0,[])
        return result

