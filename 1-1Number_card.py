list2 = []

# N개 데이터 저장
N = int(input())
Nlist = set(map(int, input().split()))

# print("set:", Nlist)

if not (1 <= len(Nlist) <= 500000):
    print("범위 초과")
else:
    # M개 데이터를 stack에 저장
    stack = []

    M = int(input())
    Mvalues = list(map(int, input().split()))

    for val in Mvalues:
        stack.append(val)

    # print("stack:", stack)
    stack_len = len(stack)

    while stack:
        val = stack.pop()
        if val in Nlist:
            list2.append(1)
        else:
            list2.append(0)

if len(list2) == stack_len:
    print(' '.join(map(str, reversed(list2))))
