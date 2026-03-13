"""
236. 二叉树的最近公共祖先 (Medium)

给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

链接: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        """
        方法: 当前节点为null/p/q 或左右子树是否为空
        
        时间: O(n)
        空间: O(h)
        """
        if not root or root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left or right
