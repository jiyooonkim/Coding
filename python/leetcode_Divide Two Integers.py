from math import floor, ceil


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:

        if dividend == -2 ** 31 and divisor == -1:
            return 2 ** 31 - 1

        if dividend / divisor > 0:
            return floor(dividend / divisor)  # 내림
        elif dividend / divisor < 0:
            return ceil(dividend / divisor)  # 올림
        else:
            return dividend // divisor
