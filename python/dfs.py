"""
    dfs(Depth-First Search) - 깊이 우선 탐색
    https://nareunhagae.tistory.com/17
    https://codingopera.tistory.com/67
"""


def ans_bfs(graph, start_node='G'):
    visited = list()  # 방문한 노드를 담을 배열
    queue = list()  # 방문 예정인 노드를 담을 배열

    queue.append(start_node)  # 처음에는 시작 노드 담아주고 시작하기.

    while queue:  # 더 이상 방문할 노드가 없을 때까지.
        node = queue.pop(0)  # 방문할 노드를 앞에서 부터 하나싹 꺼내기.

        if node not in visited:  # 방문한 노드가 아니라면
            visited.append(node)  # visited 배열에 추가
            queue.extend(graph[node])  # 해당 노드의 자식 노드로 추가

    print("bfs - ", visited)
    return visited


def my_dfs(graph):
    """
        node = 현재 위치
        stack = 남은 노드
        visitied =  방문 끝 낸 노드
    """
    visited = [list(graph.keys())[0], ] # 방문 첫번째 키 값, 초기화
    stack = list(graph.values())[0]     # 초기화
    print("1-visited : ", visited)
    print("1-stack : ", stack)

    while stack:    # stack  길이가 0일때 까지 반복
        if stack[0] not in visited:
            visited.append(stack[0])
            node = stack.pop(0)

            # print(" stack: ", stack)
            # print(" graph[node]: ", graph[node])
            # print(" visited: ", visited)
            # print(" dd: ", set(graph[node]) - set(visited))
            stack = list((item for item in graph[node] if item not in visited)) + stack

    print("visited : ", visited)
    return visited


if __name__ == "__main__":
    myGraph = {
        'A': ['B', 'C', 'D'],
        'B': ['A', 'E'],
        'C': ['A', 'F', 'G'],
        'D': ['A', 'H'],
        'E': ['B', 'I'],
        'F': ['C', 'J'],
        'G': ['C'],
        'H': ['D'],
        'I': ['E'],
        'J': ['F']
    }
    # myGraph = {
    #     'A': ['B'],
    #     'B': ['A', 'C', 'H'],
    #     'C': ['B', 'D'],
    #     'D': ['C', 'E', 'G'],
    #     'E': ['D', 'F'],
    #     'F': ['E'],
    #     'G': ['D'],
    #     'H': ['B', 'I', 'J', 'M'],
    #     'I': ['H'],
    #     'J': ['H', 'K'],
    #     'K': ['J', 'L'],
    #     'L': ['K'],
    #     'M': ['H']
    # }
    my_dfs(myGraph)
    # ans_dfs(myGraph)
