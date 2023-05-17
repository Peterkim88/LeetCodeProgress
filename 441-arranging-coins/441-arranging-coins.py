# 441. Arranging Coins
# Easy
# 3.3K
# 1.2K
# company
# Amazon
# company
# Atlassian
# company
# Bloomberg
# You have n coins and you want to build a staircase with these coins. The staircase consists of k rows where the ith row has exactly i coins. The last row of the staircase may be incomplete.

# Given the integer n, return the number of complete rows of the staircase you will build.

 

# Example 1:


# Input: n = 5
# Output: 2
# Explanation: Because the 3rd row is incomplete, we return 2.
# Example 2:


# Input: n = 8
# Output: 3
# Explanation: Because the 4th row is incomplete, we return 3.
 

# Constraints:

# 1 <= n <= 231 - 1

class Solution:
    def arrangeCoins(self, n: int) -> int:
        
        total_coins = n
        start_coin = 1

        while total_coins > start_coin:
            total_coins -= start_coin
            start_coin += 1
            print(total_coins)
            
        rem_coin = start_coin - total_coins

        if rem_coin == 0:
            return 0
        else:
            return rem_coin + 1