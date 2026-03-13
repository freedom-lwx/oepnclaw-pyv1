# 84. 柱状图中最大的矩形

**难度:** Hard

**链接:** https://leetcode.com/problems/largest-rectangle-in-histogram/

## 思路

**单调栈**

- 存储柱子下标
- 遍历过程找每个柱子左边界和右边界（第一个比它矮的柱子）

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(n) |
