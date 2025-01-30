class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        nums=list(range(1,10))
        result=[]
        def helper(index, curr_set, curr_sum):
            if len(curr_set) == k and curr_sum==n:
                result.append(curr_set[:])
                return
        
            for i in range(index, len(nums)):
                # if i> index and nums[i]==nums[i-1]:
                #     continue
                if curr_sum+nums[i]> n:
                    continue
                curr_set.append(nums[i])
                helper(i+1, curr_set,curr_sum+nums[i])
                curr_set.pop()

        helper(0,[],0)
        return result

