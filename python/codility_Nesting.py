def solution(S):
    # 참이면 1, 거짓이면 0
    answer = []
    for s in S:
        if s == "(":
            answer.append("(")
        if s == ")":
            if len(answer) > 0:
                answer.pop()
            else:
                return 0
    if len(answer) > 0:
        return 0
    else:
        return 1