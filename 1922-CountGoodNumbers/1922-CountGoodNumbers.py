class Solution(object):
    def countGoodNumbers(self, n):
        """
        :type n: int
        :rtype: int
        """
        MOD = 10**9 + 7
        if n==0:
            return 0
        
        if n==1:
            return 5
        
        even_count=5
        prime_count=4
        
        even_pos= (n+1)//2
        odd_pos = n//2

        def modular_exponentiation(base, exp, mod):
            result = 1
            while exp > 0:
                if exp % 2 == 1:
                    result = (result * base) % mod
                base = (base * base) % mod
                exp //= 2
            return result
     
        even_power = modular_exponentiation(even_count, even_pos, MOD)
        prime_power = modular_exponentiation(prime_count, odd_pos, MOD)
        
        return (even_power * prime_power) % MOD

