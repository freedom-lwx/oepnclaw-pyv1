# 215. 数组中的第K个最大元素

**难度:** Medium

**链接:** https://leetcode.com/problems/kth-largest-element-in-an-array/

## 思路

**快排，随机数选择pivot**

- 第k大 = 下标 n-k 的元素
- 三路划分处理重复元素

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) 平均 |
| 空间 | O(1) |


---

## 代码

## solution.py

```python
"""
215. 数组中的第K个最大元素 (Medium)

给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

链接: https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        方法: 快排，随机数选择pivot
        
        两种优化思路：
        1. 把 < pivot 改成 ≤ pivot
        2. 三路划分：小于、等于、大于基准数的所有元素
        
        时间: O(n) 平均
        空间: O(1)
        """
        target = len(nums) - k  # 第k大 = 下标n-k的元素
        
        def partition(left, right):
            pivot_idx = random.randint(left, right)
            nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
            pivot = nums[right]
            
            i = left
            for j in range(left, right):
                if nums[j] <= pivot:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            return i
        
        left, right = 0, len(nums) - 1
        while True:
            pos = partition(left, right)
            if pos == target:
                return nums[pos]
            elif pos < target:
                left = pos + 1
            else:
                right = pos - 1

```
