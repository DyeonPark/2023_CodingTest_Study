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
    
    def first_trial():
        def find_subgraph(path_v: list, path_e: set):
            sv = path_v[-1]
            if len(graph[sv]) == 0: return path_v
            for nv in graph[sv]:
                if (sv, nv) in path_e: return path_v
                path_v.append(nv)
                path_e.add((sv, nv))
                find_subgraph(path_v, path_e)
            return path_v
        
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
        
        for start_node in graph[create_v]:
            path = find_subgraph([start_node], set())
            define_graph(path)

    """ 각 도넛, 막대, 8자 그래프는 고유의 그래프로 존재하고 있고, 각 그래프의 정점끼리 이어진 경우는 없다.
     따라서 하나의 연결된 덩어리의 path 순서를 갖고있을 필요 없이 각 덩어리의 정점 개수, 간선 개수만 뽑아오고
     그래프 성질(eg. 막대의 경우 정점, 간선 각각 n, n-1개)에 따라 판별한다 """
    for start_node in graph[create_v]:
        print(f"start node with : {start_node}")
        node, edge = set([]), set([])
        stk = [start_node]
        while stk:
            sv = stk.pop()
            node.add(sv)
            for nv in graph[sv]:
                if (sv, nv) not in edge: 
                    stk.append(nv)
                    edge.add((sv, nv))
        print(f"node:{node}, edge:{edge}")

        n_node, n_edge = len(node), len(edge)
        if n_node == n_edge : answer['donut'] +=1
        elif n_node - n_edge == 1 : answer['bar'] +=1
        elif n_node - n_edge == -1 : answer['eight'] +=1

    return list(answer.values())

ans = solution([[2, 3], [4, 3], [1, 1], [2, 1]]); print(ans)
print('\n')
ans = solution([[4, 11], [1, 12], [8, 3], [12, 7], [4, 2], [7, 11], [4, 8], [9, 6], [10, 11], [6, 10], [3, 5], [11, 1], [5, 3], [11, 9], [3, 8]])
print(ans)
print('\n')
ans = solution([[2, 1], [2, 5], [3, 4], [4, 5], [5, 6], [6, 7], [7, 3], [3, 8], [8, 9], [9, 10], [10, 11], [11, 3]])
print(ans) # [2, 0, 1, 1]
print('\n')
ans = solution([[2, 1], [1, 3], [2, 4], [4, 5], [2, 6], [6, 7]])
print(ans) # [2, 0, 3, 0]
