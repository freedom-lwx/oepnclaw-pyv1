"""
78. 子集 (Medium)

给你一个整数数组 nums，数组中的元素互不相同。返回该数组所有可能的子集（幂集）。

链接: https://leetcode.com/problems/subsets/
"""

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        方法: 选与不选
        
        时间: O(2^n)
        空间: O(n)
        """
        result = []
        path = []
        n = len(nums)
        
        def dfs(i):
            if i == n:
                result.append(path[:])
                return
            # 不选
            dfs(i + 1)
            # 选
            path.append(nums[i])
            dfs(i + 1)
            path.pop()
        
        dfs(0)
        return result
