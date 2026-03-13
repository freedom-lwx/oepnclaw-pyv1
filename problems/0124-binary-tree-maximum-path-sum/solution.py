"""
124. 二叉树中的最大路径和 (Hard)

二叉树中的路径被定义为一条节点序列，求最大路径和。

链接: https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        方法: DP，链的概念，类似直径
        
        时间: O(n)
        空间: O(h)
        """
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            left = max(max_gain(node.left), 0)
            right = max(max_gain(node.right), 0)
            self.max_sum = max(self.max_sum, node.val + left + right)
            return node.val + max(left, right)
        
        max_gain(root)
        return self.max_sum
