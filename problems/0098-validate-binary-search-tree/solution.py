"""
98. 验证二叉搜索树 (Medium)

给你一个二叉树的根节点 root，判断其是否是一个有效的二叉搜索树。

链接: https://leetcode.com/problems/validate-binary-search-tree/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        方法: 中序遍历（BST中序遍历是递增的）
        
        时间: O(n)
        空间: O(h)
        """
        self.prev = float('-inf')
        
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if node.val <= self.prev:
                return False
            self.prev = node.val
            return inorder(node.right)
        
        return inorder(root)
