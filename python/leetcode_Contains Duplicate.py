from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        '''  sol #1 '''

        # if len(list(set(nums))) < len(nums):
        #     return True
        # else:
        #     return False

        '''  sol #2 '''
        _dict = {}
        for i in nums:
            if i in _dict.keys():
                _dict[i] += 1
                if _dict[i] == 2:
                    return True
            else:
                _dict[i] = 1

        return False




