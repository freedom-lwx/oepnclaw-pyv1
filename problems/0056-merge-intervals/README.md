# 56. 合并区间

**难度:** Medium

**链接:** https://leetcode.com/problems/merge-intervals/

## 思路

**按左端点排序，合并区间**

1. 按左端点排序
2. 遍历区间，与当前合并区间比较合并

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(nlogn) |
| 空间 | O(n) |
