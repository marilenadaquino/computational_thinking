def solve(values, safe_up_to, size):
    solution = [None] * size

    def extend_solution(position):
        for value in values:
            solution[position] = value
            if safe_up_to(solution, position):
                if position >= size-1 or extend_solution(position+1):
                    return solution
        return None

    return extend_solution(0)

def no_adjacencies(string, up_to_index):
    # See if the sequence filled from indices 0 to up_to_index, inclusive, is
    # free of any adjancent substrings. We'll have to try all subsequences of
    # length 1, 2, 3, up to half the length of the string. Return False as soon
    # as we find an equal adjacent pair.
    length = up_to_index+1
    for j in range(1, length//2+1):
        if (string[length-2*j:length-j] == string[length-j:length]):
            return False
    return True

print(''.join(str(v) for v in solve(range(3), no_adjacencies, 50)))
print(solve(range(3), no_adjacencies, 50))