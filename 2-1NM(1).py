N, M = map(int, input().split())
visited = [False] * (N + 1)   # 숫자 사용 여부 체크
result = []


def dfs(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return
    for i in range(1, N + 1):   # 1부터 N까지
        if not visited[i]:
            visited[i] = True
            result.append(i)
            dfs(depth + 1)      # 다음 자리 채우기
            result.pop()        # 백트래킹
            visited[i] = False


dfs(0)
