# 131. 分割回文串

**难度:** Medium

**链接:** https://leetcode.com/problems/palindrome-partitioning/

## 思路

**DFS + 回溯**

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n × 2^n) |
| 空间 | O(n) |


---

## 代码

## solution.py

```python
"""
131. 分割回文串 (Medium)

给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文串。
返回 s 所有可能的分割方案。

链接: https://leetcode.com/problems/palindrome-partitioning/
"""

from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        方法: DFS + 回溯
        
        时间: O(n × 2^n)
        空间: O(n)
        """
        n = len(s)
        result = []
        path = []
        
        def is_palindrome(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True
        
        def dfs(start):
            if start == n:
                result.append(path[:])
                return
            for end in range(start, n):
                if is_palindrome(start, end):
                    path.append(s[start:end + 1])
                    dfs(end + 1)
                    path.pop()
        
        dfs(0)
        return result

```
