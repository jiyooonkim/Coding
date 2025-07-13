from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        _max = sum(nums[:k])
        now = sum(nums[:k])

        for i in range(k, len(nums)):
            now = now + nums[i] - nums[i - k]
            _max = max(_max, now)
        return _max / k
