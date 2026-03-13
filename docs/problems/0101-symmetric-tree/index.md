# 101. 对称二叉树

**难度:** Easy

**链接:** https://leetcode.com/problems/symmetric-tree/

## 思路

**递归判断左右子树是否互为镜像**

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
101. 对称二叉树 (Easy)

给你一个二叉树的根节点 root，检查它是否轴对称。

链接: https://leetcode.com/problems/symmetric-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        """
        方法: 递归判断左右子树是否互为镜像
        
        时间: O(n)
        空间: O(h)
        """
        def isMirror(left, right):
            if not left and not right:
                return True
            if not left or not right:
                return False
            return (left.val == right.val and 
                    isMirror(left.left, right.right) and 
                    isMirror(left.right, right.left))
        
        return isMirror(root.left, root.right) if root else True

```
