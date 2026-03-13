"""
25. K个一组翻转链表 (Hard)

给你链表的头节点 head，每 k 个节点一组进行翻转，返回修改后的链表。

链接: https://leetcode.com/problems/reverse-nodes-in-k-group/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        """
        方法: 反转链表（k个一组）
        
        思路:
        1. 统计长度，计算需要反转的组数
        2. 每组进行反转
        3. 处理小组反转后的连接
        
        时间: O(n)
        空间: O(1)
        """
        # 统计长度
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        dummy = ListNode(0, head)
        prev = dummy
        curr = head
        
        for _ in range(n // k):
            # 反转 k 个节点
            group_prev = None
            for _ in range(k):
                next_temp = curr.next
                curr.next = group_prev
                group_prev = curr
                curr = next_temp
            
            # 连接
            tail = prev.next
            tail.next = curr
            prev.next = group_prev
            prev = tail
        
        return dummy.next
