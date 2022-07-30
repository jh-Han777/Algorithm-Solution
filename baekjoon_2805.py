import sys

n, m = map(int,sys.stdin.readline().split())
graph = list(map(int,sys.stdin.readline().split()))

def binary_search(start,end):
    while start <= end:
        mid = (start + end) // 2
        tmp = 0
        for length in graph:
            if length > mid:
                tmp += length - mid

        if tmp >= m:
            global answer
            answer = mid
            start = mid + 1
        else:
            end = mid - 1


start = 0
end = max(graph)

binary_search(start,end)
print(answer)
