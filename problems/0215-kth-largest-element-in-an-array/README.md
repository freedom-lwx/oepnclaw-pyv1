# 215. 数组中的第K个最大元素

**难度:** Medium

**链接:** https://leetcode.com/problems/kth-largest-element-in-an-array/

## 思路

**快排，随机数选择pivot**

- 第k大 = 下标 n-k 的元素
- 三路划分处理重复元素

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) 平均 |
| 空间 | O(1) |
