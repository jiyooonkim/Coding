# PassingCars

def solution(A):
    # Implement your solution here
    est_cnt = 0
    wst_cnt = 0
    answer = 0
    for i in range(0, len(A)):
        if A[i] == 0:
            est_cnt += 1
        elif A[i] == 1:
            wst_cnt += 1
            answer = answer + est_cnt

    if answer > 1000000000:
        return -1
    else:
        return answer

