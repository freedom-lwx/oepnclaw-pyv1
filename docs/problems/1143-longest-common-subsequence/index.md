# 1143. 最长公共子序列

**难度:** Medium

**链接:** https://leetcode.com/problems/longest-common-subsequence/

## 思路

**二维 DP**

dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的LCS长度

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(mn) |
| 空间 | O(mn) |


---

## 代码

## solution.py

```python
"""
1143. 最长公共子序列 (Medium)

给定两个字符串 text1 和 text2，返回这两个字符串的最长公共子序列的长度。

链接: https://leetcode.com/problems/longest-common-subsequence/
"""

from typing import List


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        方法: 二维 DP
        
        dp[i][j] 表示 text1[0:i] 和 text2[0:j] 的LCS长度
        
        时间: O(mn)
        空间: O(mn)
        """
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[m][n]

```
