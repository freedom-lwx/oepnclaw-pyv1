"""
105. 从前序与中序遍历序列构造二叉树 (Medium)

给定两个整数数组 preorder 和 inorder，构造二叉树并返回其根节点。

链接: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        方法: 前序根左右，中序左根右，分左右子树递归
        
        时间: O(n)
        空间: O(n)
        """
        inorder_map = {val: i for i, val in enumerate(inorder)}
        self.pre_idx = 0
        
        def build(left, right):
            if left > right:
                return None
            val = preorder[self.pre_idx]
            self.pre_idx += 1
            node = TreeNode(val)
            idx = inorder_map[val]
            node.left = build(left, idx - 1)
            node.right = build(idx + 1, right)
            return node
        
        return build(0, len(inorder) - 1)
