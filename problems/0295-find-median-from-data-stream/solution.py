"""
295. 数据流的中位数 (Hard)

中位数是有序整数列表中的中间值。

链接: https://leetcode.com/problems/find-median-from-data-stream/
"""

import heapq


class MedianFinder:
    """
    方法: 大小堆
    - 最大堆比最小堆多一个数（或相等）
    - 最大堆存较小的一半，最小堆存较大的一半
    
    时间: O(logn) addNum, O(1) findMedian
    空间: O(n)
    """
    
    def __init__(self):
        self.max_heap = []  # 存较小的一半，Python默认最小堆，存负值
        self.min_heap = []  # 存较大的一半
    
    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))
        else:
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
    
    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        return (-self.max_heap[0] + self.min_heap[0]) / 2


if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    print(mf.findMedian())  # 1.5
    mf.addNum(3)
    print(mf.findMedian())  # 2.0
