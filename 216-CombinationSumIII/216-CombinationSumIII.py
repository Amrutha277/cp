# Last updated: 7/12/2025, 6:29:45 PM
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results = []
        def solve(ind, total, subset):
            if total == 0 and len(subset) == k:
                results.append(subset.copy())
                return
            
            if total < 0 :
                return
            
            if ind > 9 :
                return
            
            if len(subset) > k :
                return
            
            for i in range(ind, 10):
                subset.append(i)
                solve(i+1, total - i, subset)
                subset.pop()
        solve(1, n, [])
        return results