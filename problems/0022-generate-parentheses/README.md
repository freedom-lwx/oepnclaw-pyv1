# 22. 括号生成

**难度:** Medium

**链接:** https://leetcode.com/problems/generate-parentheses/

## 思路

**DFS**

- ')' 数量 == n 时填完
- '(' < n 时填 '('
- ')' < '(' 时填 ')'

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(4^n / √n) |
| 空间 | O(n) |
