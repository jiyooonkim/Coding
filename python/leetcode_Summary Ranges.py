from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ans = []
        if nums:
            sub = [nums[0], ]
        else:
            sub = []

        for i in range(0, len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                sub.append(nums[i + 1])
            else:
                if len(sub) > 1:
                    ans.append(str(min(sub)) + "->" + str(max(sub)))
                elif len(sub) <= 1:
                    ans.append(str(min(sub)))
                sub = [nums[i + 1], ]
        if sub:
            if len(sub) > 1:
                ans.append(str(min(sub)) + "->" + str(max(sub)))
            elif len(sub) <= 1:
                ans.append(str(min(sub)))

        return ans