def solution(N):
    if (int(N ** (1 / 2)) * int(N // int(N ** (1 / 2)))) == N:
        min_pre = 2 * (int(N ** (1 / 2)) + int(N // int(N ** (1 / 2))))
    else:
        min_pre = (N + 1) * 2

    for x in range(1, int(N ** (1 / 2)) + 1):
        if N % x == 0:
            y = N // x
            if x != y:
                if 2 * (x + y) <= min_pre:
                    min_pre = 2 * (x + y)
    return min_pre