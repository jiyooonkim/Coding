from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        _sum = int(''.join(list(map(str, digits)))) + 1
        return [int(digit) for digit in str(_sum)]
