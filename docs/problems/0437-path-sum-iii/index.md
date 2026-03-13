# 437. 路径总和 III

**难度:** Medium

**链接:** https://leetcode.com/problems/path-sum-iii/

## 思路

**哈希表统计根节点开始的路径和出现次数，计算起点的次数**

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(h) |


---

## 代码

## solution.py

```python
"""
437. 路径总和 III (Medium)

给定一个二叉树的根节点 root，和一个整数 targetSum，求该二叉树里节点值之和等于 targetSum 的路径数目。

链接: https://leetcode.com/problems/path-sum-iii/
"""

from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        """
        方法: 哈希表统计根节点开始的路径和出现次数
        
        时间: O(n)
        空间: O(h)
        """
        self.count = 0
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        
        def dfs(node, curr_sum):
            if not node:
                return
            curr_sum += node.val
            self.count += prefix_sum[curr_sum - targetSum]
            prefix_sum[curr_sum] += 1
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            prefix_sum[curr_sum] -= 1
        
        dfs(root, 0)
        return self.count

```
