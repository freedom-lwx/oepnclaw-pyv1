# 70. 爬楼梯

**难度:** Easy

**链接:** https://leetcode.com/problems/climbing-stairs/

## 思路

**DP**

dp[i] 表示爬到第i级楼梯的方法数：
- dp[i] = dp[i-1] + dp[i-2]

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |
