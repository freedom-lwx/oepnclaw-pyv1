# 295. 数据流的中位数

**难度:** Hard

**链接:** https://leetcode.com/problems/find-median-from-data-stream/

## 思路

**大小堆**

- 最大堆比最小堆多一个数（或相等）
- 最大堆存较小的一半，最小堆存较大的一半

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(logn) addNum, O(1) findMedian |
| 空间 | O(n) |
