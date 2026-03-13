"""
94. 二叉树的中序遍历 (Easy)

给定一个二叉树的根节点 root，返回它的中序遍历。

链接: https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        方法: 递归 / 非递归（栈）
        
        前序: 根左右
        中序: 左根右
        后序: 左右根
        
        时间: O(n)
        空间: O(n)
        """
        # 递归
        result = []
        def inorder(node):
            if node:
                inorder(node.left)
                result.append(node.val)
                inorder(node.right)
        inorder(root)
        return result
    
    def inorderTraversal_iterative(self, root: Optional[TreeNode]) -> List[int]:
        """非递归：栈"""
        result, stack, curr = [], [], root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.val)
            curr = curr.right
        return result
