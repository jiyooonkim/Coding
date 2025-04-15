def solution(A):
    # Implement your solution here\
    sorted_A = sorted(list(set(A)))
    if len(A) == len(sorted_A):
        for i in range(0, len(sorted_A)):
            if sorted_A[i] != i+1:
                return 0
    else:
        return 0
    return 1