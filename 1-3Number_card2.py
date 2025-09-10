def lower_bound(arr, target):
    left, right = 0, len(arr)   # [left, right) 범위
    while left < right:
        mid = (left + right) // 2
        if arr[mid] >= target:  # target보다 크거나 같으면 왼쪽에도 있을 수 있음
            right = mid
        else:                   # target보다 작으면 오른쪽으로 이동
            left = mid + 1
    return left                 # target 이상이 처음 나타나는 인덱스 반환


def upper_bound(arr, target):
    left, right = 0, len(arr)   # [left, right) 범위
    while left < right:
        mid = (left + right) // 2
        if arr[mid] > target:   # target보다 큰 값이면 더 왼쪽에도 있을 수 있음
            right = mid
        else:                   # target 이하이면 오른쪽으로 이동
            left = mid + 1
    return left


N = int(input())
listN = sorted(map(int, input().split()))  # 오름차순 정렬

M = int(input())
listM = list(map(int, input().split()))

result = []
for val in listM:
    low = lower_bound(listN, val)     # val 이상이 처음 나오는 위치
    high = upper_bound(listN, val)    # val 초과가 처음 나오는 위치
    result.append(str(high - low))    # 개수 = (오른쪽 - 왼쪽)

print(" ".join(result))
