import sys

n = int(sys.stdin.readline())
times = list(map(int, sys.stdin.readline().split()))
times.sort()

total_time = 0
current_wait_time = 0


for t in times:

    current_wait_time += t

    total_time += current_wait_time

print(total_time)
