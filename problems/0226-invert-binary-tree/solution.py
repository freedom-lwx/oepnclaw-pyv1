"""
226. 翻转二叉树 (Easy)

给你一棵二叉树的根节点 root，翻转这棵二叉树，并返回其根节点。

链接: https://leetcode.com/problems/invert-binary-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        方法: 递归交换
        
        时间: O(n)
        空间: O(h)
        """
        if not root:
            return None
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
