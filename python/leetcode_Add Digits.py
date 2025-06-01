class Solution:

    def addDigits(self, num: int) -> int:
        _sum = 0
        while  num > 9:
            _sum = sum(list(map(int,str(num))))
            num = _sum
        return num 