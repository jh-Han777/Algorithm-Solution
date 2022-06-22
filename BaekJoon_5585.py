x = int(input())
x = 1000 - x
coins = [500,100,50,10,5,1]

returns = 0

for i in coins:
    returns += x // i
    x = x % i

print(returns)
