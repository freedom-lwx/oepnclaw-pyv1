# 138. 随机链表的复制

**难度:** Medium

**链接:** https://leetcode.com/problems/copy-list-with-random-pointer/

## 思路

**节点后一位是复制的新节点，再分离节点**

1. 在每个原节点后创建复制节点
2. 设置复制节点的 random 指针
3. 分离原链表和复制链表

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(1) |
