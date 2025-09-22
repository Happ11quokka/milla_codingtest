import sys

T = int(sys.stdin.readline())

coins = [25, 10, 5, 1]

for _ in range(T):

    C = int(sys.stdin.readline())
    result = []

    for coin in coins:
        count = C // coin
        result.append(str(count))
        C %= coin

    # 결과 출력
    print(" ".join(result))
