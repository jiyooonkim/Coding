def solution(A):
    num1 = 0
    num2 = sum(A)
    answer = None

    for i in range(1, len(A)):
        num1 = num1 + A[i-1]
        num2 = num2  - A[i-1]
        num = abs(num1 - num2)
        if answer is None or answer > num:
            answer = num
    
    return answer