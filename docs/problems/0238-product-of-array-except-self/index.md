# 238. 除自身以外数组的乘积

**难度:** Medium

**链接:** https://leetcode.com/problems/product-of-array-except-self/

## 思路

**前后缀分解相乘**

1. answer[i] = 左边所有元素的乘积 × 右边所有元素的乘积
2. 用两个数组分别存储前后缀乘积

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
238. 除自身以外数组的乘积 (Medium)

给你一个整数数组 nums，返回数组 answer，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积。

链接: https://leetcode.com/problems/product-of-array-except-self/
"""

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        方法: 前后缀分解相乘
        
        思路:
        1. answer[i] = 左边所有元素的乘积 × 右边所有元素的乘积
        2. 用两个数组分别存储前后缀乘积
        
        时间: O(n)
        空间: O(1) (输出数组不算)
        """
        n = len(nums)
        answer = [1] * n
        
        # 计算前缀乘积
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # 计算后缀乘积并相乘
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))  # [24, 12, 8, 6]

```
