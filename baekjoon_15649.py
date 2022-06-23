n, m = list(map(int,input().split()))

answer = []

def back():
    if len(answer) == m:
        print(" ".join(map(str,answer)))
        return
    for i in range(1, n+1):
        if i not in answer:
            answer.append(i)
            back()
            answer.pop()
back()
