class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:
        n = len(items)
        v = [1] * n
        for i in range(n):
            for j in range(n):
                if i != j and items[j][0] % items[i][0] == 0:
                    v[i] += 1

        order = sorted(range(n), key=lambda i: -items[i][1])
        dp = [0] * (budget + 1)
        ans = 0

        for k in order:
            p = items[k][1]
            if p > budget:
                continue
            rem = budget - p
            for b in range(rem + 1):
                ans = max(ans, dp[b] + v[k] + (rem - b) // p)
            for b in range(budget, p - 1, -1):
                dp[b] = max(dp[b], dp[b - p] + v[k])

        return ans