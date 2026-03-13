"""
138. 随机链表的复制 (Medium)

给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random，
该指针可以指向链表中的任何节点或空节点。请构造这个链表的深拷贝。

链接: https://leetcode.com/problems/copy-list-with-random-pointer/
"""

from typing import Optional


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = x
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        """
        方法: 节点后一位是复制的新节点，再分离节点
        
        思路:
        1. 在每个原节点后创建复制节点
        2. 设置复制节点的 random 指针
        3. 分离原链表和复制链表
        
        时间: O(n)
        空间: O(1)
        """
        if not head:
            return None
        
        # 在每个原节点后创建复制节点
        curr = head
        while curr:
            copy = Node(curr.val, curr.next)
            curr.next = copy
            curr = copy.next
        
        # 设置复制节点的 random 指针
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        
        # 分离链表
        dummy = Node(0)
        copy_curr = dummy
        curr = head
        while curr:
            copy_curr.next = curr.next
            curr.next = curr.next.next
            copy_curr = copy_curr.next
            curr = curr.next
        
        return dummy.next
