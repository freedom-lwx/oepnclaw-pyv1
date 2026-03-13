"""
199. 二叉树的右视图 (Medium)

给定一个二叉树的根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。

链接: https://leetcode.com/problems/binary-tree-right-side-view/
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        方法: 先递归右子树，再递归左子树
        
        时间: O(n)
        空间: O(h)
        """
        result = []
        
        def dfs(node, depth):
            if not node:
                return
            if depth == len(result):
                result.append(node.val)
            dfs(node.right, depth + 1)
            dfs(node.left, depth + 1)
        
        dfs(root, 0)
        return result
