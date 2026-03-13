"""
234. 回文链表 (Easy)

给你一个单链表的头节点 head，请你判断该链表是否为回文链表。

链接: https://leetcode.com/problems/palindrome-linked-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        """
        方法: 寻找中间节点 + 反转后半链表
        
        思路:
        1. 快慢指针找中点
        2. 反转后半部分
        3. 比较前后两部分
        
        时间: O(n)
        空间: O(1)
        """
        # 找中点
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 反转后半部分
        prev = None
        curr = slow
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        # 比较
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        
        return True
