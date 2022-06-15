n,m = list(map(int,input().split()))
tmp = [list(map(int,input().split())) for _ in range(n)]
answer = 0

now = (-1,-1)
while True:
    trash = 0
    for y in range(n):
        for x in range(m):
            if tmp[y][x] == 1:
                trash += 1
                if now == (-1,-1):
                    answer += 1
                    now = (y, x)
                    tmp[y][x] = 0

                elif now[0] <= y and now[1] <= x and not now == (-1,-1):
                    tmp[y][x] = 0
                    now = (y,x)
                else:
                    pass
    now = (-1,-1)
    if trash ==0:
        break

print(answer)
