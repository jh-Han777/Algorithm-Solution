n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int,input())))

num_house = 0
result = []

class DFS(object):
    def __init__(self):
        self.num_group = 0

    def dfs(self,y,x):
        if y <= -1 or y >= n or x <= -1 or x >= n:
            return False
        if graph[y][x] == 1:
            self.num_group += 1
            graph[y][x] = 0
            self.dfs(y-1,x)
            self.dfs(y+1,x)
            self.dfs(y,x+1)
            self.dfs(y,x-1)
            return self.num_group

dfs = DFS()
for j in range(n):
    for i in range(n):
        num = dfs.dfs(j,i)

        if num == False or num == None:
            continue

        if num > 0:
            num_house += 1
            result.append(num)
            dfs.num_group = 0

result.sort()

print(num_house)
if num_house > 0:
    for i in range(num_house):
        print(result[i])
