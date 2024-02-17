"""
https://school.programmers.co.kr/learn/courses/30/lessons/258711

도넛모양
- n vertices, n edges
- 임의의 정점에서 출발해 방문하지 않은 간선 계속 따라가면 나머지 정점들(n-1개) 한번씩 방문한 뒤 출발 정점으로 돌아옴

막대모양
- n vertices, n-1 edges
- 임의의 정점에서 출발해 간선 계속 따라가면 나머지 정점들(n-1개) 방문하면 한번씩 방문하게 되는 정점이 단 하나 존재함

8자모양
- 2n+1 vertices, 2n+2 edges
- 크기가 동일한 2개의 도넛 모양 그래프에서 정점을 하나씩 골라 결합시킨 형태

"""

def solution(edges):

    answer = [0, 0, 0, 0]
    answer = {'create_vertex': 0, 'donut': 0, 'bar': 0, 'eight': 0}

    def make_graph() -> list:
        v = max([max(x) for x in edges])
        graph = [[] for _ in range(v+1)]
        for start, end in edges:
            graph[start].append(end)
        return graph
    graph = make_graph()

    def find_create_v() -> None:
        max_l, create_v = 0, 0
        for i, l in enumerate(graph):
            if len(l) > max_l:
                max_l = len(l)
                create_v = i 
        return create_v
    create_v = find_create_v()
    answer['create_vertex'] = create_v
    

    for start_node in graph[create_v]:
        def find_subgraph(path_v: list, path_e: set):
            sv = path_v[-1]
            if len(graph[sv]) == 0: return path_v
            for nv in graph[sv]:
                if (sv, nv) in path_e: return path_v
                path_v.append(nv)
                path_e.add((sv, nv))
                find_subgraph(path_v, path_e)
            return path_v

        path = find_subgraph([start_node], set())
        # print(f"path with started from {start_node} : {path}")

        def define_graph(path):
            p_len = len(path)
            s_len = len(set(path))

            if p_len == 1 or p_len == s_len:
                answer['bar'] += 1
                return

            if (len(path) == 2 and len(set(path)) == 1) or \
                p_len - s_len == 1:
                answer['donut'] += 1
                return
            
            answer['eight'] += 1
            return

        define_graph(path)

    return list(answer.values())

ans = solution([[2, 3], [4, 3], [1, 1], [2, 1]]); print(ans)
print('\n')
ans = solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])
print(ans)

ans = solution([[2, 1], [2, 5], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3], [3, 8], [8, 9], [9, 10], [10, 11], [11, 3]])
print(ans) # [2, 0, 1, 1]

ans = solution([[2, 1], [1, 3], [2, 4], [4, 5], [2, 6], [6, 7]])
print(ans) # [2, 0, 3, 0]
