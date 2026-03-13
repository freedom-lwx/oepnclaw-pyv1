# 53. 最大子数组和

**难度:** Medium

**链接:** https://leetcode.com/problems/maximum-subarray/

## 思路

**前缀和 + 贪心 / 动态规划**

1. dp[i] 表示以 nums[i] 结尾的最大子数组和
2. dp[i] = max(nums[i], dp[i-1] + nums[i])

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |
