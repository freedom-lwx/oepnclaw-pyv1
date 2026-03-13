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


---

## 代码

## solution.py

```python
"""
22. 括号生成 (Medium)

数字 n 代表生成括号的对数，请你设计一个函数，用于能够生成所有可能的并且有效的括号组合。

链接: https://leetcode.com/problems/generate-parentheses/
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        方法: DFS
        - ')' 数量 == n 时填完
        - '(' < n 时填 '('
        - ')' < '(' 时填 ')'
        
        时间: O(4^n / sqrt(n))
        空间: O(n)
        """
        result = []
        path = []
        
        def dfs(open_count, close_count):
            if close_count == n:
                result.append(''.join(path))
                return
            
            if open_count < n:
                path.append('(')
                dfs(open_count + 1, close_count)
                path.pop()
            
            if close_count < open_count:
                path.append(')')
                dfs(open_count, close_count + 1)
                path.pop()
        
        dfs(0, 0)
        return result

```
