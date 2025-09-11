def wood(heights, H):
    # 1. 절단 높이 H에서 얻는 총 목재 길이
    total = 0
    for h in heights:
        if h > H:
            total += h - H
    return total


# 2. 나무의 수 N, 필요한 목재의 길이 M
N, M = map(int, input().split())

# 3. 나무들의 높이
heights = list(map(int, input().split()))

# 4. 절단 높이 H는 0부터 최대 나무 높이 사이에 존재
a, b = 0, max(heights)


ans = 0
# 5. 교차할 때까지 반복
while a <= b:
    # 6. 중간값(mid)을 절단 높이 후보로 설정
    mid = (a + b) // 2

    # 7. 현재 mid에서 잘려 얻는 목재 총 길이 계산
    cut = wood(heights, mid)

    # 8. 절단 높이를 더 올려도 될 수 있음
    if cut >= M:
        ans = mid
        a = mid + 1
    else:
        # 9. 낮춰야 함
        b = mid - 1

print(ans)
