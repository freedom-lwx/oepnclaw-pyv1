# 763. 划分字母区间

**难度:** Medium

**链接:** https://leetcode.com/problems/partition-labels/

## 思路

**贪心，合并区间**

- 遍历字符串，计算字母的最后出现下标 last[i]
- 合并区间

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |


---

## 代码

## solution.py

```python
"""
763. 划分字母区间 (Medium)

给你一个字符串 s，把这个字符串划分为尽可能多的片段，
同一字母最多出现在一个片段中。

链接: https://leetcode.com/problems/partition-labels/
"""

from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        """
        方法: 遍历字符串，计算字母的最后出现下标 last[i]，合并区间
        
        时间: O(n)
        空间: O(1)
        """
        last = {c: i for i, c in enumerate(s)}
        
        result = []
        start = 0
        end = 0
        
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        
        return result

```
