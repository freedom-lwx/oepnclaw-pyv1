# 438. 找到字符串中所有字母异位词

**难度:** Medium

**链接:** https://leetcode.com/problems/find-all-anagrams-in-a-string/

## 思路

**不定长滑动窗口**

1. 维护窗口内字符计数
2. 窗口大小等于 len(p) 时检查是否为异位词

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |
