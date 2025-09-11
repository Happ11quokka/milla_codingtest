# 1. 랜선 조각 수 계산
def count_pieces(cables, L):
    total = 0
    for x in cables:
        total += x // L
    return total


# 2. 입력 받기
K, N = map(int, input().split())
cables = [int(input()) for _ in range(K)]

# 3. 이진 탐색 범위 설정 (조각 최소 길이 1, 최대 길이 = 가장 긴 랜선)
low, high = 1, max(cables)
ans = 0

# 4. 이진 탐색
while low <= high:
    mid = (low + high) // 2   # 후보 조각 길이
    pieces = count_pieces(cables, mid)

    if pieces >= N:
        # 5. 조건 만족: 더 길게 잘라도 가능
        ans = mid
        low = mid + 1
    else:
        # 6. 조건 불만족: 조각 수 부족, 길이를 줄인다
        high = mid - 1

print(ans)
