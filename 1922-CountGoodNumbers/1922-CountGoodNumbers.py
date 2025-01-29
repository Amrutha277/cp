class Solution(object):
    def countGoodNumbers(self, n):
        
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        ans = 1
        rem = n % 2
        n -= rem
        ans = pow(20, n // 2, MOD)
        
        if rem == 1:
            ans = (ans * 5) % MOD
        
        return ans
