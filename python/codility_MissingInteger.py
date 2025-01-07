# MissingInteger

def solution(A):
    A.append(0)
    _A = sorted(list(set(A)))
    _sum = A[0] - 1
    abs_list = _A[_A.index(0):]

    if len(abs_list) == 1 and _A[0] == 0:
        return 1
    else:
        for i in range(0, len(abs_list)):
            if abs_list[i] != i:
                return i
    return _A[-1] + 1


