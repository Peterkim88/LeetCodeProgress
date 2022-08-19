/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let buyPrice = prices[0]
    let maxProfit = 0;
    for (let i = 0; i < prices.length-1; i++){
        let profit = prices[i+1] - prices[i];
        if (profit > 0){
            if (prices[i] < buyPrice){
                buyPrice = prices[i];
            }
            if (prices[i+1] - buyPrice > maxProfit){
                maxProfit = prices[i+1] - buyPrice;
            }
        }
    }
    return maxProfit;
};