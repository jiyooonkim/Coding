# Triangle
def solution(A):
    # Implement your solution here

    if len(A) > 2:
        A = sorted(A)
        for i in range(0, len(A) - 2):
            # print("A : ", A[i], A[i+1],A[i+2])
            if A[i] + A[i + 1] > A[i + 2]:
                return 1

    return 0
