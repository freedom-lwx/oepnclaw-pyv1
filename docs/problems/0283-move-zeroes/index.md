# 283. 移动零

**难度:** Easy

**链接:** https://leetcode.com/problems/move-zeroes/

## 思路

**双指针交换元素**

1. 左指针指向当前已处理好的非零元素末尾
2. 右指针遍历数组
3. 遇到非零元素，与左指针位置交换

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
283. 移动零 (Easy)

给定一个数组 nums，将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。

链接: https://leetcode.com/problems/move-zeroes/
"""

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        方法: 双指针交换元素
        
        思路:
        1. 左指针指向当前已处理好的非零元素末尾
        2. 右指针遍历数组
        3. 遇到非零元素，与左指针位置交换
        
        时间: O(n)
        空间: O(1)
        """
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)  # [1, 3, 12, 0, 0]

```
