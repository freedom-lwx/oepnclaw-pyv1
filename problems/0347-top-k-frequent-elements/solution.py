"""
347. 前K个高频元素 (Medium)

给你一个整数数组 nums 和一个整数 k，请你返回其中出现频率前 k 高的元素。

链接: https://leetcode.com/problems/top-k-frequent-elements/
"""

from typing import List
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        方法: 桶排序
        - 哈希表统计元素出现次数
        - 出现次数相同元素放入同一个桶
        - 倒序遍历桶
        
        时间: O(n)
        空间: O(n)
        """
        count = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        
        for num, freq in count.items():
            buckets[freq].append(num)
        
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
        return result
