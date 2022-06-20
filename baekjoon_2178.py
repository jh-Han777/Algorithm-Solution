from collections import deque

n,m = list(map(int,input().split()))
graph = []
for _ in range(n):
    graph.append(list(map(int,input())))
print(graph)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(y,x):
    queue =deque()
    queue.append((y,x))

    while queue:
        y,x = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= m or ny < 0 or ny >= n:
                continue

            if graph[ny][nx] == 0:
                continue

            if graph[ny][nx] == 1:
                graph[ny][nx] = graph[y][x] + 1
                queue.append((ny,nx))
    return graph[n-1][m-1]

print(bfs(0,0))
