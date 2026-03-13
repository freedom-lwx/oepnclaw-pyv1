# 322. 零钱兑换

**难度:** Medium

**链接:** https://leetcode.com/problems/coin-change/

## 思路

**完全背包 DP**

- 物品无限：正序遍历
- dp[i] 表示凑成金额i的最少硬币数

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(amount × n) |
| 空间 | O(amount) |
