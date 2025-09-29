import sys

n = int(sys.stdin.readline())

levels = list(map(int, sys.stdin.readline().split()))


max_level = 0
for level in levels:
    if level > max_level:
        max_level = level


total_gold = 0
for level in levels:
    total_gold += max_level + level
total_gold -= max_level

print(total_gold)
