# 51. N皇后

**难度:** Hard

**链接:** https://leetcode.com/problems/n-queens/

## 思路

**DFS + 回溯，逐行放置皇后**

- 检查列冲突
- 检查对角线冲突 (row - col 和 row + col)

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n!) |
| 空间 | O(n) |
