# 41. 缺失的第一个正数

**难度:** Hard

**链接:** https://leetcode.com/problems/first-missing-positive/

## 思路

**索引和值匹配放置**

1. 将数值 x 放到索引 x-1 的位置
2. 遍历找出第一个 nums[i] != i+1 的位置

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
41. 缺失的第一个正数 (Hard)

给你一个未排序的整数数组 nums，请你找出其中没有出现的最小的正整数。
要求算法的时间复杂度为 O(n)，且只能使用常数级别的额外空间。

链接: https://leetcode.com/problems/first-missing-positive/
"""

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        """
        方法: 索引和值匹配放置
        
        思路:
        1. 将数值 x 放到索引 x-1 的位置
        2. 遍历找出第一个 nums[i] != i+1 的位置
        
        时间: O(n)
        空间: O(1)
        """
        n = len(nums)
        
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        
        return n + 1


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive([1, 2, 0]))  # 3
    print(s.firstMissingPositive([3, 4, -1, 1]))  # 2

```
