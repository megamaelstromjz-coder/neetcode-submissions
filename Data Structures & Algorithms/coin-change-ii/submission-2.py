class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        mem = {}

        def dp(i, amt):
            if amt == 0:
                return 1
            if amt < 0 or i == n:
                return 0
            if (i, amt) in mem:
                return mem[(i, amt)]

            mem[(i, amt)] = dp(i + 1, amt) + dp(i, amt - coins[i])
            return mem[(i, amt)]

        return dp(0, amount)