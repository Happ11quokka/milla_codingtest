result = []

# 1. A[N]을 setN에 담는다
N = int(input())
setN = set(map(int, input().split()))

# 2. 주어진 M 개의 수를 listM에 담는다

M = int(input())
listM = list(map(int, input().split()))

# 3. 이를 for 문 통해 하나씩 확인
for val in listM:
    if val in setN:
        result.append('1')
    else:
        result.append('0')

print('\n'.join(result))
