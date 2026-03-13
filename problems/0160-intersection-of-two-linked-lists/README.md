# 160. 相交链表

**难度:** Easy

**链接:** https://leetcode.com/problems/intersection-of-two-linked-lists/

## 思路

**到null跳到另一条链**

1. 两个指针分别遍历两条链
2. 到末尾时跳到另一条链的头部
3. 相遇时即为交点

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(m + n) |
| 空间 | O(1) |
