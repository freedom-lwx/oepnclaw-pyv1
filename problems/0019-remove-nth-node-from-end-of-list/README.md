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
