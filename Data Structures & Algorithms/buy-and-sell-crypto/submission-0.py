class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        op = [0] * len(prices)

        i=0

        while i < len(prices):

            sell = prices[i]
            buy = min(prices[:i]) if i!= 0 else prices[i]
            profit = max((sell - buy), 0)
            op[i] = profit

            i+=1

        print((op))

        return max(op)

        