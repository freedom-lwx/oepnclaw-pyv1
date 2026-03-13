# 200. 岛屿数量

**难度:** Medium

**链接:** https://leetcode.com/problems/number-of-islands/

## 思路

**递归遍历上下左右并标记**

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(mn) |
| 空间 | O(mn) |


---

## 代码

## solution.py

```python
"""
200. 岛屿数量 (Medium)

给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

链接: https://leetcode.com/problems/number-of-islands/
"""

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        方法: 递归遍历上下左右并标记
        
        时间: O(mn)
        空间: O(mn)
        """
        if not grid:
            return 0
        
        m, n = len(grid), len(grid[0])
        count = 0
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] != '1':
                return
            grid[i][j] = '#'
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        
        return count

```
