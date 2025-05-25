class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = list(str(x))
        for i in range(0, len(x)):
            if x[i] != x[len(x) -1 -i]:
                return False
        return True
