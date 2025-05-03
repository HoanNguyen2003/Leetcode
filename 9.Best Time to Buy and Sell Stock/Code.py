class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        # # O(n^2)
        # max = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         if (prices[j]- prices[i]) > max:
        #             max = prices[j]- prices[i]
        # return max


        # # O(n) but not optimize
        # min_price = prices[0]
        # max_profit = 0

        # for i in range(len(prices)):
        #     if prices[i] < min_price:
        #         min_price = prices[i]
            
        #     current_profit = prices[i] - min_price
        #     if current_profit > max_profit:
        #         max_profit = current_profit

        # return max_profit


        # # O(n) and Optimize
        min_price = prices[0]  
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
        
prices = [7,1,5,3,6,4]
run = Solution()
print(run.maxProfit(prices))

# Output: 5