# 19. 删除链表的倒数第N个节点

**难度:** Medium

**链接:** https://leetcode.com/problems/remove-nth-node-from-end-of-list/

## 思路

**前后指针**

1. 前指针先走 n 步
2. 前后指针同时走，前指针到末尾时，后指针指向倒数第 n+1 个节点

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |


---

## 代码

## solution.py

```python
"""
19. 删除链表的倒数第N个节点 (Medium)

给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

链接: https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
        方法: 前后指针
        
        思路:
        1. 前指针先走 n 步
        2. 前后指针同时走，前指针到末尾时，后指针指向倒数第 n+1 个节点
        
        时间: O(n)
        空间: O(1)
        """
        dummy = ListNode(0, head)
        fast = slow = dummy
        
        # 前指针先走 n 步
        for _ in range(n):
            fast = fast.next
        
        # 同时走
        while fast.next:
            fast = fast.next
            slow = slow.next
        
        # 删除节点
        slow.next = slow.next.next
        return dummy.next

```
