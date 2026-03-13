# 41. 缺失的第一个正数

**难度:** Hard

**链接:** https://leetcode.com/problems/first-missing-positive/

## 思路

**索引和值匹配放置**

1. 将数值 x 放到索引 x-1 的位置
2. 遍历找出第一个 nums[i] != i+1 的位置

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |
