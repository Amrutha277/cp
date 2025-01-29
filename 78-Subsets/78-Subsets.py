class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result =[]
        index=0

        def backtrack(index, cur_ans):
            if index == len(nums):
                result.append(cur_ans[:])
                return
            
            
            cur_ans.append(nums[index])
            backtrack(index+1, cur_ans)
            cur_ans.pop()
            backtrack(index+1, cur_ans)
            
        backtrack(0,[])
        return result
            