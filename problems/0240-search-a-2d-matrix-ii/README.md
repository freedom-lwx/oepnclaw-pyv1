# 240. 搜索二维矩阵 II

**难度:** Medium

**链接:** https://leetcode.com/problems/search-a-2d-matrix-ii/

## 思路

**排除法**

1. 从右上角开始
2. 当前值 > target，向左；当前值 < target，向下

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(m + n) |
| 空间 | O(1) |
