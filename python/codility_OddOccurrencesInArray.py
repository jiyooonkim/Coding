# OddOccurrencesInArray
def solution(A):
    cnt_dic = {}
    result = 0

    for val in A:
        if val in cnt_dic:
            cnt_dic[val] += 1
        else:
            cnt_dic[val] = 1

    for key, val in cnt_dic.items():
        if val % 2 == 1:
            return key
