"""
543. 二叉树的直径 (Easy)

给你一棵二叉树的根节点，返回该树的直径（树中任意两个节点间最长路径的长度）。

链接: https://leetcode.com/problems/diameter-of-binary-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        方法: DP，链的概念
        
        链: node子树中叶子节点到node的路径
        直径 = 拼接node左右两条链的最大值
        
        时间: O(n)
        空间: O(h)
        """
        self.diameter = 0
        
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)
        
        depth(root)
        return self.diameter
