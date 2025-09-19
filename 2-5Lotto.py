

def find_combinations(start_index, current_combination, k, S):
    if len(current_combination) == 6:
        print(*current_combination)
        return

    for i in range(start_index, k):
        current_combination.append(S[i])
        find_combinations(i + 1, current_combination, k, S)
        current_combination.pop()

case_count = 0
while True:
    line = list(map(int, input().split()))
    
    if line[0] == 0:
        break
        
    k = line[0]
    S = line[1:]
    
    if case_count > 0:
        print()
        
    find_combinations(0, [], k, S)
    
    case_count += 1