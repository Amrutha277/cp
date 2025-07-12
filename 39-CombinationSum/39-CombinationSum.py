# Last updated: 7/12/2025, 5:38:09 PM
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result=[]

        def backtrack(index, path, cur_sum):
            if cur_sum== target:
                result.append(path[:])
                return
            if index == len(candidates) or cur_sum> target:
                return
            
            #take. reusing elements so index doesnt move forward in take
            path.append(candidates[index])
            backtrack(index, path, cur_sum+ candidates[index])
            path.pop()

            #no take. so index moves forward
            backtrack(index+1, path, cur_sum)

        backtrack(0,[],0)
        return result