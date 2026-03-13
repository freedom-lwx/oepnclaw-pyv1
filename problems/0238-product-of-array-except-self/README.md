# 238. 除自身以外数组的乘积

**难度:** Medium

**链接:** https://leetcode.com/problems/product-of-array-except-self/

## 思路

**前后缀分解相乘**

1. answer[i] = 左边所有元素的乘积 × 右边所有元素的乘积
2. 用两个数组分别存储前后缀乘积

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |
