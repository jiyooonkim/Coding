# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    # Implement your solution here
    Y = Y - X
    ans = Y // D
    if Y % D:
        ans += 1
    return ans
