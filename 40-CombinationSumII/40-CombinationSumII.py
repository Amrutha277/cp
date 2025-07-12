# Last updated: 7/12/2025, 5:48:39 PM
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        result=[]
        def backtrack(index, path, cur_sum):
            if cur_sum==target:
                result.append(path[:])
                return
            
            if cur_sum> target or index == len(candidates):
                return
            
            candidates.sort()
            for i in range(index, len(candidates)):
                if i > index and candidates[i] == candidates[i-1]:
                    continue
    
                path.append(candidates[i])
                backtrack(i+1, path, cur_sum+ candidates[i])
                path.pop()

                # backtrack(index+1, path, cur_sum)
        
        backtrack(0,[],0)
        return result
            