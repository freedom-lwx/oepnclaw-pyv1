"""
2. 两数相加 (Medium)

给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，
并且每个节点只能存储一位数字。

链接: https://leetcode.com/problems/add-two-numbers/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法: 递归（两节点值和进位值相加）
        
        思路:
        1. 递归处理每一位
        2. 处理进位
        
        时间: O(max(m, n))
        空间: O(max(m, n))
        """
        def add(l1, l2, carry):
            if not l1 and not l2 and carry == 0:
                return None
            
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            total = val1 + val2 + carry
            
            node = ListNode(total % 10)
            node.next = add(
                l1.next if l1 else None,
                l2.next if l2 else None,
                total // 10
            )
            return node
        
        return add(l1, l2, 0)
