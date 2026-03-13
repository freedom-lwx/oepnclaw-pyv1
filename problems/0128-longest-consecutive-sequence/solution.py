"""
128. 最长连续序列 (Medium)

给定一个未排序的整数数组 nums，找出数字连续的最长序列的长度。
要求算法的时间复杂度为 O(n)。

链接: https://leetcode.com/problems/longest-consecutive-sequence/
"""

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        方法: Set - 遍历元素起点找最长连续序列
        
        思路:
        1. 将所有元素加入Set
        2. 遍历每个元素，如果 num-1 不在Set中，说明是序列起点
        3. 从起点开始向下枚举，找最长连续序列
        
        时间: O(n)
        空间: O(n)
        """
        num_set = set(nums)
        longest = 0
        
        for num in num_set:
            # 只有当 num-1 不在集合中时，才是序列起点
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                
                longest = max(longest, current_streak)
        
        return longest


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive([100, 4, 200, 1, 3, 2]))  # 4
    print(s.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))  # 9
