"""
189. 轮转数组 (Medium)

给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置。

链接: https://leetcode.com/problems/rotate-array/
"""

from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        方法: 三次反转
        
        思路:
        1. 反转整个数组
        2. 反转前k个元素
        3. 反转后n-k个元素
        
        时间: O(n)
        空间: O(1)
        """
        n = len(nums)
        k = k % n
        
        def reverse(left, right):
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    print(nums)  # [5, 6, 7, 1, 2, 3, 4]
