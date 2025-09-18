count = 0


def find_subsequences(index, current_sum, numbers, target_sum):
    global count

    if index == len(numbers):
        if current_sum == target_sum:
            count += 1
        return

    find_subsequences(index + 1, current_sum +
                      numbers[index], numbers, target_sum)

    find_subsequences(index + 1, current_sum, numbers, target_sum)


N, S = map(int, input().split())
numbers = list(map(int, input().split()))

find_subsequences(0, 0, numbers, S)

if S == 0:
    print(count - 1)
else:
    print(count)
