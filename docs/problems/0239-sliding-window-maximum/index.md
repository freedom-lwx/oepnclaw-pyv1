# 239. 滑动窗口最大值

**难度:** Hard

**链接:** https://leetcode.com/problems/sliding-window-maximum/

## 思路

**单调队列 - 右入左出，维护队首（最大值）**

1. 维护单调递减队列（存索引）
2. 新元素入队时，弹出所有比它小的元素
3. 队首过期时弹出

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(k) |


---

## 代码

## solution.py

```python
"""
239. 滑动窗口最大值 (Hard)

给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到最右侧，
返回滑动窗口中的最大值。

链接: https://leetcode.com/problems/sliding-window-maximum/
"""

from typing import List
from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        方法: 单调队列 - 右入左出，维护队首（最大值）
        
        思路:
        1. 维护单调递减队列（存索引）
        2. 新元素入队时，弹出所有比它小的元素
        3. 队首过期时弹出
        
        时间: O(n)
        空间: O(k)
        """
        dq = deque()
        result = []
        
        for i, num in enumerate(nums):
            # 弹出比当前元素小的（它们不可能成为最大值）
            while dq and nums[dq[-1]] < num:
                dq.pop()
            dq.append(i)
            
            # 队首过期，弹出
            if dq[0] <= i - k:
                dq.popleft()
            
            # 窗口形成后开始记录结果
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3,3,5,5,6,7]

```
