"""
45. 跳跃游戏 II (Medium)

给定一个非负整数数组 nums，你最初位于数组的第一个下标。
返回到达最后一个下标的最小跳跃次数。

链接: https://leetcode.com/problems/jump-game-ii/
"""

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        方法: 贪心
        - 更新从当前所有位置能跳到的最远位置
        - 当走到当前跳跃能到达的最远位置进行一次新的跳跃
        
        时间: O(n)
        空间: O(1)
        """
        n = len(nums)
        if n <= 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            
            if i == current_end:
                jumps += 1
                current_end = farthest
        
        return jumps
