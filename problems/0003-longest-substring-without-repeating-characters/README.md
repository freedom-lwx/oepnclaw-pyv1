# 3. 无重复字符的最长子串

**难度:** Medium

**链接:** https://leetcode.com/problems/longest-substring-without-repeating-characters/

## 思路

**哈希表 + 滑动窗口**

1. 哈希表统计字符出现次数
2. 有字符次数 > 1 时，移除左端点字符
3. 滑动窗口维护无重复字符的子串

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(min(n, m)) |
