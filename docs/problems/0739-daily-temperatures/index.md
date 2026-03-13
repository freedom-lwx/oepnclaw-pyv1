# 739. 每日温度

**难度:** Medium

**链接:** https://leetcode.com/problems/daily-temperatures/

## 思路

**单调栈**

- 从左到右
- 栈存储索引

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
739. 每日温度 (Medium)

给定一个整数数组 temperatures，表示每天的温度，
返回一个数组 answer，使得 answer[i] 表示对于第 i 天，
下一个更高温度出现在几天后。

链接: https://leetcode.com/problems/daily-temperatures/
"""

from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        方法: 单调栈，从右到左或从左到右
        
        时间: O(n)
        空间: O(n)
        """
        n = len(temperatures)
        result = [0] * n
        stack = []  # 存索引
        
        for i in range(n):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)
        
        return result

```
