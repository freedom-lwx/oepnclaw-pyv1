# 20. 有效的括号

**难度:** Easy

**链接:** https://leetcode.com/problems/valid-parentheses/

## 思路

**栈**

- 奇数长度直接返回 false
- 哈希表保存对应关系
- 左括号入栈，右括号判断栈顶

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(n) |


---

## 代码

## solution.py

```python
"""
20. 有效的括号 (Easy)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s，判断字符串是否有效。

链接: https://leetcode.com/problems/valid-parentheses/
"""

from typing import List


class Solution:
    def isValid(self, s: str) -> bool:
        """
        方法: 奇数return false，哈希表保存对应关系，左括号入栈，右括号判断栈顶
        
        时间: O(n)
        空间: O(n)
        """
        if len(s) % 2 == 1:
            return False
        
        mapping = {')': '(', ']': '[', '}': '{'}
        stack = []
        
        for ch in s:
            if ch in mapping:
                if not stack or stack[-1] != mapping[ch]:
                    return False
                stack.pop()
            else:
                stack.append(ch)
        
        return not stack

```
