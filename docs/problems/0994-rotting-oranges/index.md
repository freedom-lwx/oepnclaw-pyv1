# 994. 腐烂的橘子

**难度:** Medium

**链接:** https://leetcode.com/problems/rotting-oranges/

## 思路

**多源BFS，Queue，四方向遍历**

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
994. 腐烂的橘子 (Medium)

在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：
- 值 0 代表空单元格
- 值 1 代表新鲜橘子
- 值 2 代表腐烂的橘子

链接: https://leetcode.com/problems/rotting-oranges/
"""

from typing import List
from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        方法: 多源BFS，Queue，四方向遍历
        
        时间: O(mn)
        空间: O(mn)
        """
        m, n = len(grid), len(grid[0])
        queue = deque()
        fresh = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0
        
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        queue.append((ni, nj))
            minutes += 1
        
        return minutes - 1 if fresh == 0 else -1

```
