class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low = 0
        maxProf = 0
        
        for i in range(1, len(prices)):
            if prices[i] < prices[low]:
                low = i
            if prices[i] - prices[low] > maxProf:
                maxProf = prices[i] - prices[low]
        
        return maxProf