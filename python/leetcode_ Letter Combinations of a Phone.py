class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_to_chars = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        def get_letter(ans, letter):
            sub = []
            for j in ans:
                for k in letter:
                    sub.append(j + k)
            return sub

        if digits:
            ans = [""]
            for i in digits:
                ans = get_letter(ans, digit_to_chars[i])
            return ans
        else:
            return []
