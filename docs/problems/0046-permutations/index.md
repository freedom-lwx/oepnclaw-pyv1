# 46. 全排列

**难度:** Medium

**链接:** https://leetcode.com/problems/permutations/

## 思路

**boolean[] onPath标记选过没，枚举path[i]填哪个数**

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
46. 全排列 (Medium)

给定一个不含重复数字的数组 nums，返回其所有可能的全排列。

链接: https://leetcode.com/problems/permutations/
"""

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        方法: boolean[] onPath标记选过没，枚举path[i]填哪个数
        
        时间: O(n!)
        空间: O(n)
        """
        n = len(nums)
        result = []
        path = [0] * n
        on_path = [False] * n
        
        def dfs(i):
            if i == n:
                result.append(path[:])
                return
            for j in range(n):
                if not on_path[j]:
                    path[i] = nums[j]
                    on_path[j] = True
                    dfs(i + 1)
                    on_path[j] = False
        
        dfs(0)
        return result

```
