# 104. 二叉树的最大深度

**难度:** Easy

**链接:** https://leetcode.com/problems/maximum-depth-of-binary-tree/

## 思路

**递归**

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
104. 二叉树的最大深度 (Easy)

给定一个二叉树 root，返回其最大深度。

链接: https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        方法: 递归
        
        时间: O(n)
        空间: O(h) h为树高
        """
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

```
