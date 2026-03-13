"""
300. 最长递增子序列 (Medium)

给你一个整数数组 nums，找到其中最长严格递增子序列的长度。

链接: https://leetcode.com/problems/longest-increasing-subsequence/
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        方法: DP + 二分
        
        dp[i] 表示以nums[i]结尾的最长递增子序列长度
        
        时间: O(nlogn)
        空间: O(n)
        """
        if not nums:
            return 0
        
        tails = [nums[0]]
        
        for num in nums[1:]:
            if num > tails[-1]:
                tails.append(num)
            else:
                # 二分查找第一个 >= num 的位置
                left, right = 0, len(tails) - 1
                while left <= right:
                    mid = (left + right) // 2
                    if tails[mid] < num:
                        left = mid + 1
                    else:
                        right = mid - 1
                tails[left] = num
        
        return len(tails)
