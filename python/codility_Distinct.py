def solution(A):
    dict = {}
    for i in A:
        if (dict.get(i)):      # 딕셔너리에 값이 있다면 (key가 i인 값의 value가 존재한다면)
            dict[i] += 1       # 기존 value 값에 1 더하기
        else:
            dict[i] = 1
    return len(dict)