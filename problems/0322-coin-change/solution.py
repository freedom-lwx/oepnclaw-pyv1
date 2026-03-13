"""
322. 零钱兑换 (Medium)

给定不同面额的硬币和一个总金额。计算可以凑成总金额的最少硬币个数。

链接: https://leetcode.com/problems/coin-change/
"""

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        方法: 完全背包 DP
        物品无限，正序遍历
        
        dp[i] 表示凑成金额i的最少硬币数
        
        时间: O(amount × n)
        空间: O(amount)
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
