# 263. Ugly Number
# Easy
# 2.8K
# 1.5K
# company
# Bloomberg
# company
# Facebook
# company
# Amazon
# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return true if n is an ugly number.

 

# Example 1:

# Input: n = 6
# Output: true
# Explanation: 6 = 2 × 3
# Example 2:

# Input: n = 1
# Output: true
# Explanation: 1 has no prime factors, therefore all of its prime factors are limited to 2, 3, and 5.
# Example 3:

# Input: n = 14
# Output: false
# Explanation: 14 is not ugly since it includes the prime factor 7.
 

# Constraints:

# -231 <= n <= 231 - 1

class Solution:

    def isUgly(self, n: int) -> bool:

        if n <= 0:
            return False

        validFactors = [2, 3, 5]

        for f in validFactors:
            while n % f == 0:
                n = n / f

        if n == 1:
            return True
        else:
            return False
        
        
        # if n < 1:
        #     return False
        # if n == 1:
        #     return True

        # def isPrime(num: int):
        #     i = 2

        #     while i < num:
        #         if num % i == 0:
        #             return False
        #         i += 1

        #     return True

        # validPrime = [2, 3, 5]

        # if isPrime(n) and not n in validPrime:
        #     return False

        # j = 2

        # while j <= (n // j):
        #     if n % j == 0:
        #         k = n // j
        #         if isPrime(j) and not j in validPrime or isPrime(k) and not k in validPrime:
        #             return False
        #     j += 1

        # return True 