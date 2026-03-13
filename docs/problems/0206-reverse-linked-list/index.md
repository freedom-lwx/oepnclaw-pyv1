# 206. 反转链表

**难度:** Easy

**链接:** https://leetcode.com/problems/reverse-linked-list/

## 思路

**头插法**

1. 遍历链表
2. 每个节点插入到新链表的头部

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
206. 反转链表 (Easy)

给你单链表的头节点 head，请你反转链表，并返回反转后的链表。

链接: https://leetcode.com/problems/reverse-linked-list/
"""

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        方法: 头插法
        
        思路:
        1. 遍历链表
        2. 每个节点插入到新链表的头部
        
        时间: O(n)
        空间: O(1)
        """
        prev = None
        curr = head
        
        while curr:
            next_temp = curr.next
            curr.next = prev
            prev = curr
            curr = next_temp
        
        return prev


def list_to_nodes(arr):
    dummy = ListNode()
    curr = dummy
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next


def nodes_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


if __name__ == "__main__":
    s = Solution()
    head = list_to_nodes([1, 2, 3, 4, 5])
    result = s.reverseList(head)
    print(nodes_to_list(result))  # [5, 4, 3, 2, 1]

```
