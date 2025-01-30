class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        curr_set, result = [], []
        curr_sum = 0
        candidates.sort()
        def helper(index, curr_set, curr_sum):
            if curr_sum == target:
                result.append(list(curr_set))
                return
            for i in range(index, len(candidates)):
                if i> index and candidates[i]== candidates[i-1]:
                    continue
                if curr_sum+ candidates[i]>target:
                    break
                curr_set.append(candidates[i])
                helper(i+1, curr_set, curr_sum+candidates[i])
                curr_set.pop()
        helper(0,[],0)
        return result
