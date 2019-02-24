# backtracking
# basically a recursive function
# a refined brute-force approach

# the solution is a combination of elements that satisfy some constraints
# the objective is to find whether that solution exists or not, e.g. in a maze
# other similar alorithms may be optimesed for looking for the shortest path, but cannot say if it exists or not

# it tries all the possible combinations incrementally 
# abandons the ones that do not satisfy your condition
# goes back to the last check point

# for solving constraint satisfaction problems, such as crosswords, verbal arithmetic, Sudoku. 
# for solving the knapsack problem, parsing texts and other combinatorial optimization problems.

def permute(charIndex, s):
    "simple case of swapping, no constraints"
    if charIndex == 1:
        return s
    else:
        l = []
        for y in permute(1, s):
            for x in permute(charIndex - 1, s):
                l.append(y + x)
        return l
        # return [ y + x
        #          for y in permute(1, s)
        #          for x in permute(charIndex - 1, s)
        #          ]

print(permute(1, ["a","b","c"]))
# ['a', 'b', 'c']
# 3x1 combination
print(permute(2, ["a","b","c"]))
# ['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc']
# 3x3 combination
print(permute(3, ["a","b","c"]))
# ['aaa', 'aab', 'aac', 'aba', 'abb', 'abc', 'aca', 'acb', 'acc', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bca', 'bcb', 'bcc', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc']
# 3x9 combination


# see examples running: http://cs.lmu.edu/~ray/notes/backtracking/

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


def extend_solution(position, values, solution, safe_up_to, size):
        for value in values:
            solution[position] = value # try to fill with value
            if safe_up_to(solution, position): # if no_adjacencies is satisfied (return True)
                if position >= size-1 or extend_solution(position+1, values, solution, safe_up_to, size):
                    return solution # return the partial solution if position >= size-1 (i.e. we are done) or there is the following solution
        return None

def solve(values, safe_up_to, size):
    """Finds a solution to a backtracking problem.

    values     -- a sequence of values to try, in order. For a map coloring
                  problem, this may be a list of colors, such as ['red',
                  'green', 'yellow', 'purple']
    safe_up_to -- a function with two arguments, solution and position, that
                  returns whether the values assigned to slots 0..pos in
                  the solution list, satisfy the problem constraints.
    size -- the total number of "slots" you are trying to fill

    Return the solution as a list of values.
    """
    solution = [None] * size # create a list full of None values for the total number of slots

    return extend_solution(0, values, solution, safe_up_to, size) # modify each value of the list according to parameters recursively

print( solve(range(3), no_adjacencies, 50) )