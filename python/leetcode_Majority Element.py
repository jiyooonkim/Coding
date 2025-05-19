from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        _dict = {}
        num = len(nums) // 2
        for i in nums:
            if i not in _dict:
                _dict[i] = 1
            if _dict[i] > num:
                return i
            else:
                _dict[i] += 1

        return nums[0]

nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
Solution.majorityElement(nums)

