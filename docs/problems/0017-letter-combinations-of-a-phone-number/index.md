# 17. 电话号码的字母组合

**难度:** Medium

**链接:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/

## 思路

**DFS + 枚举回溯**

先写数字对应电话键盘字母常量数组

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(4^n) |
| 空间 | O(n) |


---

## 代码

## solution.py

```python
"""
17. 电话号码的字母组合 (Medium)

给定一个仅包含数字 2-9 的字符串 digits，返回所有它能表示的字母组合。

链接: https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""

from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        """
        方法: DFS + 枚举回溯
        先写数字对应电话键盘字母常量数组
        
        时间: O(4^n)
        空间: O(n)
        """
        if not digits:
            return []
        
        MAPPING = "", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"
        n = len(digits)
        result = []
        path = []
        
        def dfs(i):
            if i == n:
                result.append(''.join(path))
                return
            for ch in MAPPING[int(digits[i])]:
                path.append(ch)
                dfs(i + 1)
                path.pop()
        
        dfs(0)
        return result

```
