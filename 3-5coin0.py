import sys


N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]


count = 0

for coin in reversed(coins):
    if coin > K:
        continue

    num_of_coins = K // coin
    count += num_of_coins

    K %= coin
    if K == 0:
        break

print(count)
