class Solution:

    ''' Version1 '''
    def reverse(self, x: int) -> int:
        ans =  0

        if x > 0 :
            ans = int(str(x)[::-1])
        elif x < 0 :
            ans = int(str(x*-1)[::-1]) * -1
        if ans not in range(-2**31,2**31):
            return 0
        else:
             return ans

    ''' Version2 '''

    def reverse(self, x: int) -> int:
        _x = int(str(abs(x))[::-1])
        if x < 0:
            _x = _x * -1
        if _x > 2 ** 31 - 1 or _x < -(2 ** 31):
            return 0
        else:
            return _x
