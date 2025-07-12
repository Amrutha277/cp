# Last updated: 7/12/2025, 6:27:16 PM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result=[]
        
        def backtrack(index, path, cur_sum):
            if len(path) == k:
                if cur_sum == n:
                    result.append(path[:])
                return

            for i in range(index, 10):
                path.append(i)
                backtrack(i+1, path, cur_sum+i)
                path.pop()

        backtrack(1,[],0)
        return result