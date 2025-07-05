from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1, ], ]
        row = [1, ]

        def get_sum(row, n):
            _sub = [row[0], ]
            for j in range(0, n - 1):
                _sub.append(row[j] + row[j + 1])
            _sub.append(1)
            return _sub

        for i in range(1, numRows):
            row = get_sum(row, i)
            answer.append(row)
        return answer