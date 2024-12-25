# GenomicRangeQuery

def solution(S, P, Q):
    # Implement your solution here
    dic_s = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
    answer = []
    for i in range(0, len(P)):

        '''sol1. 100% '''
        _s = S[P[i]:Q[i] + 1]
        if 'A' in S[P[i]:Q[i] + 1]:
            answer.append(dic_s['A'])
        elif 'C' in S[P[i]:Q[i] + 1]:
            answer.append(dic_s['C'])
        elif 'G' in S[P[i]:Q[i] + 1]:
            answer.append(dic_s['G'])
        elif 'T' in S[P[i]:Q[i] + 1]:
            answer.append(dic_s['T'])

        '''sol2. 61% '''
        # _s = sorted(list(set(S[P[i]:Q[i]+1])))
        # if len(_s)>0:
        #     answer.append(dic_s[_s[0]])

    return answer
