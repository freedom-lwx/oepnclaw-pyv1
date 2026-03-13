# 1. 两数之和

**难度:** Easy

**链接:** https://leetcode.com/problems/two-sum/

## 题目描述

给定一个整数数组 `nums` 和一个整数目标值 `target`，请你在该数组中找出和为目标值 `target` 的那两个整数，并返回它们的数组下标。

## 思路

**哈希表 - 维护右枚举左**

1. 遍历数组，用哈希表存储已访问的元素及其索引
2. 对于当前元素 `nums[i]`，检查 `target - nums[i]` 是否在哈希表中
3. 如果存在，返回两个索引

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(n) |

## 关键点

- 使用哈希表将查找从 O(n) 降到 O(1)
- 一次遍历即可完成


---

## 代码

## solution.py

```python
"""
1. 两数之和 (Easy)

给定一个整数数组 nums 和一个整数目标值 target，
请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

链接: https://leetcode.com/problems/two-sum/
"""

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        方法: 哈希表 - 维护右枚举左
        
        思路:
        1. 遍历数组，用哈希表存储已访问的元素及其索引
        2. 对于当前元素 nums[i]，检查 target - nums[i] 是否在哈希表中
        3. 如果存在，返回两个索引
        
        时间: O(n)
        空间: O(n)
        """
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == "__main__":
    s = Solution()
    print(s.twoSum([2, 7, 11, 15], 9))  # [0, 1]
    print(s.twoSum([3, 2, 4], 6))  # [1, 2]

```
