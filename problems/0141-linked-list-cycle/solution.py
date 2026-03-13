"""
141. 环形链表 (Easy)

给你一个链表的头节点 head，判断链表中是否有环。

链接: https://leetcode.com/problems/linked-list-cycle/
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        方法: 快慢指针相遇
        
        思路:
        1. 快指针每次走2步，慢指针每次走1步
        2. 如果有环，一定会相遇
        
        时间: O(n)
        空间: O(1)
        """
        if not head or not head.next:
            return False
        
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        
        return False
