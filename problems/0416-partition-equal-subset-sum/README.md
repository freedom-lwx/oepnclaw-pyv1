# 416. 分割等和子集

**难度:** Medium

**链接:** https://leetcode.com/problems/partition-equal-subset-sum/

## 思路

**0-1背包 DP**

- 物品唯一：倒序遍历
- dp[i] 表示能否凑出和i

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n × target) |
| 空间 | O(target) |
