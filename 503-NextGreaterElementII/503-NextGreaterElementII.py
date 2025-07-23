# Last updated: 7/22/2025, 8:05:53 PM
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n= len(nums)
        stack=[]
        result=[-1]*n
        for i in range(2*n):
            num= nums[i%n]
            while stack and num> nums[stack[-1]]:
                result[stack.pop()]=num
            if i < n:
                stack.append(i)
        return result
        
            
