s = input()
p = input()

count = 0
left = 0
right = len(p)

while left < right:
    if p[left:right] in s:
        count += 1
        left = right
        right = len(p)
    else:
        right -= 1

print(count)
