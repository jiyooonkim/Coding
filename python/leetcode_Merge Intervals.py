
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        intervals = sorted(intervals)
        start = intervals[0][0]
        end = intervals[0][1]
        answer = []
        for i in range(0, len(intervals)):

            tmp = [start, end]
            if intervals[i][0] <= end:
                if intervals[i][1] >= end:
                    end = intervals[i][1]
            else:
                answer.append(tmp)
                start = intervals[i][0]
                end = intervals[i][1]

            if len(intervals) - 1 == i:
                answer.append([start, end])
        return answer


if __name__ == "__main__":
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    # intervals = [[1, 4], [4, 5]]
    Solution.merge()

