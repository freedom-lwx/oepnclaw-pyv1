"""
56. 合并区间 (Medium)

以数组 intervals 表示若干个区间的集合，请合并所有重叠的区间。

链接: https://leetcode.com/problems/merge-intervals/
"""

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        方法: 按左端点排序，合并区间
        
        思路:
        1. 按左端点排序
        2. 遍历区间，与当前合并区间比较合并
        
        时间: O(nlogn)
        空间: O(n)
        """
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))  # [[1,6],[8,10],[15,18]]
