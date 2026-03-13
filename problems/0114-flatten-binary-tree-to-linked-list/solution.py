"""
114. 二叉树展开为链表 (Medium)

给你二叉树的根结点 root，请你将它展开为一个单链表。

链接: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        方法: 头插法，按右子树-左子树-根顺序DFS
        
        时间: O(n)
        空间: O(h)
        """
        self.prev = None
        
        def dfs(node):
            if not node:
                return
            dfs(node.right)
            dfs(node.left)
            node.right = self.prev
            node.left = None
            self.prev = node
        
        dfs(root)
