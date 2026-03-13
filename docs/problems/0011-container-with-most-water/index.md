# 11. 盛最多水的容器

**难度:** Medium

**链接:** https://leetcode.com/problems/container-with-most-water/

## 思路

**双指针**

1. 左右指针从两端开始
2. 计算当前面积，移动较短的指针向中间
3. 较短边决定水量，移动较长边无法增加水量

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
11. 盛最多水的容器 (Medium)

给定一个长度为 n 的整数数组 height，有 n 条垂线，
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

链接: https://leetcode.com/problems/container-with-most-water/
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        方法: 双指针
        
        思路:
        1. 左右指针从两端开始
        2. 计算当前面积，移动较短的指针向中间
        3. 较短边决定水量，移动较长边无法增加水量
        
        时间: O(n)
        空间: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49

```
