class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        total = m + n
        mid = total // 2
        is_even = (total % 2 == 0)
        print(is_even)
        i, j, merged_index = 0, 0, 0
        now, prev = 0, 0 
        
        while merged_index <= mid:
            prev = now
            
            if i < m and (j >= n or nums1[i] <= nums2[j]):
                now = nums1[i]
                i += 1
            else:
                now = nums2[j]
                j += 1
            
            merged_index += 1
        
        
        if is_even:
            print((now+prev)/2)
            return (float(now) + prev) / 2
        else:
            return now

        