def solution(K, A):
    _length = 0
    cnt = 0

    for _a in A:
        _length = _length + _a
        if _length >= K:
            cnt = cnt + 1
            _length = 0

    return cnt 
