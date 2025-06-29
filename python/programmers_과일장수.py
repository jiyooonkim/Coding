# https://school.programmers.co.kr/learn/courses/30/lessons/135808

def solution(m, score):
    answer = 0
    score = sorted(score, reverse=True)
    for i in range(0, len(score) - m + 1, m):
        answer = answer + min(score[i:i + m]) * m
    return answer
