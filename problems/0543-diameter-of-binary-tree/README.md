# 543. 二叉树的直径

**难度:** Easy

**链接:** https://leetcode.com/problems/diameter-of-binary-tree/

## 思路

**DP，链的概念**

- 链: node子树中叶子节点到node的路径
- 直径 = 拼接node左右两条链的最大值

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(h) |
