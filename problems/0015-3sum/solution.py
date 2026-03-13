"""
15. 三数之和 (Medium)

给你一个整数数组 nums，判断是否存在三元组 [nums[i], nums[j], nums[k]] 
满足 i != j、i != k 且 j != k，同时还满足 nums[i] + nums[j] + nums[k] == 0。

链接: https://leetcode.com/problems/3sum/
"""

from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        方法: 先排序 + 双指针
        
        思路:
        1. 先排序
        2. 固定第一个数，用双指针找另外两个数
        3. 跳过重复元素
        
        时间: O(n²)
        空间: O(1)
        """
        nums.sort()
        n = len(nums)
        result = []
        
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
