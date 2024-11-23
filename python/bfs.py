"""
    bfs(Breadth-First Search) - 넓이 우선 탐색
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


def my_bfs(graph):
    """
        node = 현재 위치
        queue = 남은 노드
        visitied =  방문 끝 낸 노드
    """
    visited = [list(graph.keys())[6],]      # 방문 첫번째 키 값, 초기화
    queue = list(graph.values())[6]         # 초기화
    # print("start visited : ", visited)
    # print("start  queue : ", queue)

    while queue:    # stack  길이가 0일때 까지 반복
        if queue[0] not in visited:
            visited.append(queue[0])
            node = queue.pop(0)

            # 앞으로 탐색할 값 == 추가될 노드 에서 방문한 노드 뺀 값 추가(순서보장 필요)
            queue.extend([x for x in graph[node] if x not in visited])      # graph[node] - visited
            # print(" queue: ", queue)
            # print(" graph[node]: ", graph[node])
            # print(" visited: ", visited)

    print("visited : ", visited)
    return visited


if __name__ == "__main__":

    """ Test Case """
    # myGraph = {
    #     'A': ['B', 'C', 'D'],
    #     'B': ['A', 'E'],
    #     'C': ['A', 'F', 'G'],
    #     'D': ['A', 'H'],
    #     'E': ['B', 'I'],
    #     'F': ['C', 'J'],
    #     'G': ['C'],
    #     'H': ['D'],
    #     'I': ['E'],
    #     'J': ['F']
    # }
    myGraph = {
        'A': ['B'],
        'B': ['A', 'C', 'H'],
        'C': ['B', 'D'],
        'D': ['C', 'E', 'G'],
        'E': ['D', 'F'],
        'F': ['E'],
        'G': ['D'],
        'H': ['B', 'I', 'J', 'M'],
        'I': ['H'],
        'J': ['H', 'K'],
        'K': ['J', 'L'],
        'L': ['K'],
        'M': ['H']
    }
    print(my_bfs(myGraph))
    # ans_bfs(myGraph)
