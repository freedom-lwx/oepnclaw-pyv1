"""
53. 最大子数组和 (Medium)

给你一个整数数组 nums，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

链接: https://leetcode.com/problems/maximum-subarray/
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        方法: 前缀和 + 贪心 / 动态规划
        
        思路:
        1. dp[i] 表示以 nums[i] 结尾的最大子数组和
        2. dp[i] = max(nums[i], dp[i-1] + nums[i])
        
        时间: O(n)
        空间: O(1)
        """
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
