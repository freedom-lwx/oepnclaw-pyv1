"""
42. 接雨水 (Hard)

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
计算按此排列的柱子，下雨之后能接多少雨水。

链接: https://leetcode.com/problems/trapping-rain-water/
"""

from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        方法: 前后缀分解 / 相向双指针
        
        思路:
        1. 对于位置i，能接的雨水 = min(左边最高, 右边最高) - height[i]
        2. 用双指针从两端向中间遍历
        3. 维护左右两侧的最大值
        
        时间: O(n)
        空间: O(1)
        """
        if not height:
            return 0
        
        left, right = 0, len(height) - 1
        left_max, right_max = height[left], height[right]
        water = 0
        
        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                water += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                water += right_max - height[right]
        
        return water


if __name__ == "__main__":
    s = Solution()
    print(s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  # 6
