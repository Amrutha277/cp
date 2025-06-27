# Last updated: 6/27/2025, 6:14:08 PM
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        total=0
        minl= float('inf')
        for r in range(len(nums)):
            total +=  nums[r]
            while total>=target:
                minl= min(minl, r-l+1)
                total -= nums[l]
                l+=1
        return minl if minl != float(inf) else 0