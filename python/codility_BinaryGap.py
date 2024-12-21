# https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
def solution(N):
    b = (format(N, "b")).strip('0')
    cnt = 1
    max_cnt = 0
    for i in range(0, len(b) - 1):
        if b[i] == "0":

            if b[i] == b[i + 1]:
                cnt += 1
            if b[i] != b[i + 1]:
                cnt = 1
            if max_cnt < cnt:
                max_cnt = cnt

    return max_cnt

