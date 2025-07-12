# Last updated: 7/12/2025, 3:47:07 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        if n==0:
            return []
        left=0
        right=0
        def backtrack(current, left, right):
            if len(current) == 2*n:
                result.append(current)
                return
            
            if left<n:
                backtrack(current+'(',left+1, right)
            
            if left>right:
                # print("ji")
                backtrack(current+')', left, right+1)
            # print(current)
            
        backtrack("",0,0)
        return result