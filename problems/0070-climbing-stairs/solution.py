"""
70. 爬楼梯 (Easy)

假设你正在爬楼梯，每次可以爬 1 或 2 个台阶。
返回爬到楼梯顶部需要爬多少步。

链接: https://leetcode.com/problems/climbing-stairs/
"""

from typing import List


class Solution:
    def climbStairs(self, n: int) -> int:
        """
        方法: DP
        
        dp[i] 表示爬到第i级楼梯的方法数
        dp[i] = dp[i-1] + dp[i-2]
        
        时间: O(n)
        空间: O(1)
        """
        if n <= 2:
            return n
        
        dp = [0] * (n + 1)
        dp[0], dp[1] = 1, dp[2] = 2
        
        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        
        return dp[n]
