import sys

N, M, K = map(int, sys.stdin.readline().split())

max_teams = 0
for i in range(K + 1):

    remaining_N = N - i
    remaining_M = M - (K - i)

    if remaining_N < 0 or remaining_M < 0:
        continue

    possible_teams = min(remaining_N // 2, remaining_M)

    if possible_teams > max_teams:
        max_teams = possible_teams

print(max_teams)
