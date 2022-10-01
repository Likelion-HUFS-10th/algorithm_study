N, M = tuple(map(int, input().split()))
graph = [[] for _ in range(N+1)]
visited = [False for _ in range(N+1)]
count = 0

for _ in range(M):
    start, end = tuple(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)

def dfs(vertex):
    global count
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            # print(curr_v)
            count += 1
            visited[curr_v] = True
            dfs(curr_v)

root_vertex = 1
visited[root_vertex] = True
dfs(root_vertex)
print(count)