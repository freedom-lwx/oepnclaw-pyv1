# 73. 矩阵置零

**难度:** Medium

**链接:** https://leetcode.com/problems/set-matrix-zeroes/

## 思路

**扫两遍，记录行0和列0**

1. 第一遍扫描记录哪些行和列需要置0
2. 第二遍置0

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(mn) |
| 空间 | O(m+n) |


---

## 代码

## solution.py

```python
"""
73. 矩阵置零 (Medium)

给定一个 m x n 的矩阵，如果一个元素为 0，则将其所在行和列的所有元素都设为 0。

链接: https://leetcode.com/problems/set-matrix-zeroes/
"""

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        方法: 扫两遍，记录行0和列0
        
        思路:
        1. 第一遍扫描记录哪些行和列需要置0
        2. 第二遍置0
        
        时间: O(mn)
        空间: O(m+n)
        """
        m, n = len(matrix), len(matrix[0])
        rows, cols = set(), set()
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows.add(i)
                    cols.add(j)
        
        for i in range(m):
            for j in range(n):
                if i in rows or j in cols:
                    matrix[i][j] = 0


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    print(matrix)  # [[1,0,1],[0,0,0],[1,0,1]]

```
