"""
230. 二叉搜索树中第K小的元素 (Medium)

给定一个二叉搜索树的根节点 root，和一个整数 k，设计一个算法查找其中第 k 个最小元素。

链接: https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        方法: 中序遍历找第k个节点
        
        时间: O(h + k)
        空间: O(h)
        """
        self.count = 0
        self.result = None
        
        def inorder(node):
            if not node or self.result is not None:
                return
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.val
                return
            inorder(node.right)
        
        inorder(root)
        return self.result
