# Last updated: 6/27/2025, 8:16:37 PM
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        l=0
        r=0
        seen= set()
        for r in range(len(nums)):
            if nums[r] in seen:
                return True
            else:
                seen.add(nums[r])
            if len(seen)>k:
                seen.remove(nums[l])
                l+=1
        return False

        

            



