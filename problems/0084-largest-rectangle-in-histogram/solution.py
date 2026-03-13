"""
84. 柱状图中最大的矩形 (Hard)

给定 n 个非负整数，用来表示柱状图中各个柱子的高度。
求在该柱状图中，能够勾勒出来的矩形的最大面积。

链接: https://leetcode.com/problems/largest-rectangle-in-histogram/
"""

from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        方法: 单调栈，存储柱子下标
        遍历过程找每个柱子左边界和右边界（第一个比它矮的柱子）
        
        时间: O(n)
        空间: O(n)
        """
        heights.append(0)  # 哨兵
        stack = [-1]  # 栈底哨兵
        max_area = 0
        
        for i, h in enumerate(heights):
            while stack[-1] != -1 and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)
        
        return max_area
