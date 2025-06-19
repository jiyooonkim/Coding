from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        ans = 0
        left = 0
        right = len(height) - 1
        if height:
            while left < right:
                current_width = right - left
                current_height = min(height[right], height[left])
                ans = max(ans, current_width * current_height)

                if height[right] > height[left]:
                    left += 1
                else:
                    right -= 1

        return ans