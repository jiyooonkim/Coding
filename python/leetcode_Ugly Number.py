class Solution:
    def isUgly(self, n: int) -> bool:

        while 1:
            if n == 1:
                return True
            elif n == 0:
                return False
            else:
                if n % 2 ==  0:
                    n = n // 2
                elif n % 3 ==  0:
                    n = n // 3
                elif n % 5 ==  0:
                    n = n // 5
                else:
                    return False