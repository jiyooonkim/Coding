# 
def solution(A):
    return len(list(set([abs(x) for x in A])))