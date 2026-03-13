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


---

## 代码

## solution.py

```python
"""
51. N皇后 (Hard)

按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。
n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上。

链接: https://leetcode.com/problems/n-queens/
"""

from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        方法: DFS + 回溯，逐行放置皇后
        
        时间: O(n!)
        空间: O(n)
        """
        result = []
        board = ['.' * n for _ in range(n)]
        cols = set()
        diag1 = set()  # row - col
        diag2 = set()  # row + col
        
        def dfs(row):
            if row == n:
                result.append(board[:])
                return
            
            for col in range(n):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                cols.add(col)
                diag1.add(row - col)
                diag2.add(row + col)
                board[row] = '.' * col + 'Q' + '.' * (n - col - 1)
                
                dfs(row + 1)
                
                cols.remove(col)
                diag1.remove(row - col)
                diag2.remove(row + col)
                board[row] = '.' * n
        
        dfs(0)
        return result

```
