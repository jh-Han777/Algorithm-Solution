N = int(input())
K = int(input())
cor = list(map(int,input().split()))

cor.sort()

space = []
for i in range(1,len(cor)):
    space.append(cor[i] - cor[i-1])

space.sort(reverse=True)
print(sum(space[K-1:]))
