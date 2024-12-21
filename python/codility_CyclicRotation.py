# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # 빈배열(길이가 0 ), 정수 0 고려할 것
    if len(A) > 0 and K > 0:
        for i in range(0, int(K)):
            A.insert(0, A[-1])
            A.pop()
    return A

