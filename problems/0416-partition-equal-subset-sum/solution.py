"""
416. 分割等和子集 (Medium)

给你一个非负整数数组 nums，判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。

链接: https://leetcode.com/problems/partition-equal-subset-sum/
"""

from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        方法: 0-1背包 DP
        物品唯一：倒序遍历
        
        时间: O(n × target)
        空间: O(target)
        """
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        for num in nums:
            for i in range(target, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
        
        return dp[target]
