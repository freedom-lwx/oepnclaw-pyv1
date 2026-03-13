# 347. 前K个高频元素

**难度:** Medium

**链接:** https://leetcode.com/problems/top-k-frequent-elements/

## 思路

**桶排序**

- 哈希表统计元素出现次数
- 出现次数相同元素放入同一个桶
- 倒序遍历桶

## 复杂度

| 复杂度 | 值 |
|--------|-----|
| 时间 | O(n) |
| 空间 | O(n) |
