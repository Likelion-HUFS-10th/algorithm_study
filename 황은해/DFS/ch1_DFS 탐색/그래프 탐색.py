# 정점, 간선
n, m = tuple(map(int, input().split()))

# 간선이 적은 경우, 인접 행렬 보다 인접 리스트를 활용하는 것이 효율적!
# index를 1번 부터 사용하기 위해 n+1 만큼 할당.
graph = [[] for _ in range(n+1)]

# DFS 함수 호출 전, 이미 방문한 노드의 값은 True로 바꿔줄 것
visited = [False for _ in range(n+1)]
vertex_cnt = 0

def dfs(vertex):
    global vertex_cnt 

    # 해당 정점에서 이어져있는 모든 정점을 탐색함
    for curr_v in graph[vertex]:
        # 아직 간선이 존재하고 방문한 적 없는 정점만 탐색
        if not visited[curr_v]:
            visited[curr_v] = True
            vertex_cnt += 1
            dfs(curr_v)


for i in range(m):
    v1, v2 = tuple(map(int, input().split()))

    # 각 정점에 대한 간선을 저장해줌.
    graph[v1].append(v2)
    graph[v2].append(v1)
    
visited[1] = True
dfs(1)

print(vertex_cnt)
            
