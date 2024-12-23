def solution(S):
    char_dit = {'(': ')', '{': '}', '[': ']'}
    stack = []  # in keys

    for i in S:
        # print("i : ", i )
        if i not in char_dit.values():
            stack.append(i)

            # print("stack : ", stack)
        else:
            if len(stack) == 0:
                return 0
            else:
                _pop = stack.pop()
                if i != char_dit[_pop]:
                    # print("_pop : ", _pop)
                    stack.append(_pop)
                    return 0

    if len(stack) == 0:
        return 1
    else:
        return 0
