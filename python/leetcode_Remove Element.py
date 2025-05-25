from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # print(nums.remove(val))
        answer = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[answer] = nums[i]
                answer = answer + 1
        return answer
