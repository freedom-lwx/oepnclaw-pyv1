# 142. 环形链表 II

**难度:** Medium

**链接:** https://leetcode.com/problems/linked-list-cycle-ii/

## 思路

**Floyd判圈**

1. 快慢指针相遇
2. 头指针和慢指针同时走，相遇时为入环处

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
142. 环形链表 II (Medium)

给定一个链表的头节点 head，返回链表开始入环的第一个节点。如果链表无环，则返回 null。

链接: https://leetcode.com/problems/linked-list-cycle-ii/
"""

from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法: Floyd判圈
        
        思路:
        1. 快慢指针相遇
        2. 头指针和慢指针同时走，相遇时为入环处
        
        时间: O(n)
        空间: O(1)
        """
        if not head or not head.next:
            return None
        
        slow = fast = head
        
        # 快慢指针相遇
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        # 头指针和慢指针同时走
        p = head
        while p != slow:
            p = p.next
            slow = slow.next
        
        return p

```
