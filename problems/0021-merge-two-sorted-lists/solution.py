"""
21. 合并两个有序链表 (Easy)

将两个升序链表合并为一个新的升序链表并返回。

链接: https://leetcode.com/problems/merge-two-sorted-lists/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法: 迭代尾插法
        
        思路:
        1. 用虚拟头节点简化操作
        2. 比较两个链表当前节点，小的接入结果链表
        
        时间: O(m + n)
        空间: O(1)
        """
        dummy = ListNode()
        curr = dummy
        
        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        curr.next = list1 or list2
        return dummy.next
