# 76. 最小覆盖子串

**难度:** Hard

**链接:** https://leetcode.com/problems/minimum-window-substring/

## 思路

**滑动窗口 + less变量**

1. 用less变量维护子串中有less种字母出现次数小于t中字母的出现次数
2. less == 0 时，窗口满足条件
3. 收缩左边界找最小窗口

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |
