class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        res, s = 0, 0
        threshold = threshold * k
        s = sum(arr[:k-1])

        for r in range(k-1, len(arr)):
            s += arr[r]
            if s >= threshold: res +=1
            s -= arr[r-k+1]

        return res
        