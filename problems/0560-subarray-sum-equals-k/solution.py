"""
560. 和为 K 的子数组 (Medium)

给定一个整数数组和一个整数 k，请找到该数组中和为 k 的连续子数组的个数。

链接: https://leetcode.com/problems/subarray-sum-equals-k/
"""

from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        方法: 前缀和 + 哈希表
        
        思路:
        1. 用哈希表记录每个前缀和出现的次数
        2. 对于当前位置，找有多少个前缀和 = 当前前缀和 - k
        
        时间: O(n)
        空间: O(n)
        """
        count = defaultdict(int)
        count[0] = 1
        prefix_sum = 0
        result = 0
        
        for num in nums:
            prefix_sum += num
            result += count[prefix_sum - k]
            count[prefix_sum] += 1
        
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([1, 1, 1], 2))  # 2
