#O(n), and O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointer problem l is sell day, r is buy day - sliding window
        l , r = 0, 1
        maxP = 0
        while r < len(prices):
            if prices[l] < prices[r]: # check if we can make profit
                profit = prices[r] - prices[l]
                maxP = max(maxP, profit)
            else:
                l = r # move to where right pointer is now
            r += 1 # advance to next day
        return maxP