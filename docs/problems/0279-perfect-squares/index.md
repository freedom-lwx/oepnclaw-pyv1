# 279. 完全平方数

**难度:** Medium

**链接:** https://leetcode.com/problems/perfect-squares/

## 思路

**完全背包 DP**

- dp[i] 表示和为i的最少平方数个数
- 1, 4, 9, 16... 都是完全平方数

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n × √n) |
| 空间 | O(n) |


---

## 代码

## solution.py

```python
"""
279. 完全平方数 (Medium)

给你一个整数 n，返回和为 n 的完全平方数的最少数量。

链接: https://leetcode.com/problems/perfect-squares/
"""

from typing import List


class Solution:
    def numSquares(self, n: int) -> int:
        """
        方法: 完全背包 DP
        
        dp[i] 表示和为i的最少平方数个数
        1, 4, 9, 16... 都是完全平方数
        
        时间: O(n × sqrt(n))
        空间: O(n)
        """
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        
        return dp[n]

```
