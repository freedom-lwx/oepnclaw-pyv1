# 300. 最长递增子序列

**难度:** Medium

**链接:** https://leetcode.com/problems/longest-increasing-subsequence/

## 思路

**DP + 二分**

- dp[i] 表示以nums[i]结尾的最长递增子序列长度
- 维护一个有序数组 tails，tails[i] 表示长度为 i+1 的递增子序列的最小末尾元素

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(nlogn) |
| 空间 | O(n) |
