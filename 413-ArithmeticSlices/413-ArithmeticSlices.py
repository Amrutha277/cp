# Last updated: 6/27/2025, 11:57:55 PM
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        l=0
        r=3
        count=0
        current=0
        for l in range(2,len(nums)):
            if nums[l]-nums[l-1]== nums[l-1]- nums[l-2]:
                current+=1
                count+=current
            else:
                current=0
        return count



