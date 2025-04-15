# MaxNonoverlappingSegments

def solution(A, B):
    # Implement your solution here
    lst = []
    cnt = 1
    if len(A) == 0:
        return 0
    elif len(A) == 1:
        return 1
    else:
        for a, b in zip(A, B):
            lst.append((a, b))
        # lst.sort()
        lst.sort(key=lambda x: (x[1], x[0]))

        first = lst[0][1]

        for i in range(1, len(lst)):
            if lst[i][0] > first:
                first = lst[i][1]
                cnt = cnt + 1
        #     print(lst[i])
        # print(cnt)
        return cnt