# 121. 买卖股票的最佳时机

**难度:** Easy

**链接:** https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

## 思路

**贪心**

- 更新 minPrice
- 找最大 prices[i] - minPrice

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
121. 买卖股票的最佳时机 (Easy)

给定一个数组 prices，它的第 i 个元素 prices[i] 是一支股票第 i 天的价格。
选择某一天买入并在未来某一天卖出，计算能获取的最大利润。

链接: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        方法: 贪心，更新minPrice，找最大 prices[i] - minPrice
        
        时间: O(n)
        空间: O(1)
        """
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        
        return max_profit

```
