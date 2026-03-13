# 55. 跳跃游戏

**难度:** Medium

**链接:** https://leetcode.com/problems/jump-game/

## 思路

**贪心**

- 维护最右可达位置 max
- i > max 返回 false

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
55. 跳跃游戏 (Medium)

给定一个非负整数数组 nums，你最初位于数组的第一个下标。
判断你是否能够到达最后一个下标。

链接: https://leetcode.com/problems/jump-game/
"""

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """
        方法: 维护最右可达位置max，i > max return false
        
        时间: O(n)
        空间: O(1)
        """
        max_reach = 0
        n = len(nums)
        
        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        
        return True

```
