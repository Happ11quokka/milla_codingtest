
# 1. 입력 받기
N = int(input())
arr = list(map(int, input().split()))

# 2. 중복 제거 후 정렬
sorted = sorted(set(arr))

# 3. 좌표 -> 압축값 매핑
rank = {value: idx for idx, value in enumerate(sorted)}

# 4. 원래 배열을 매핑하여 출력
print(" ".join(str(rank[x]) for x in arr))
