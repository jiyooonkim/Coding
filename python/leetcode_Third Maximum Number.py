from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        _nums = sorted(set(nums), reverse=True)

        if len(_nums) > 2:
            return _nums[2]
        else:
            return max(nums)
